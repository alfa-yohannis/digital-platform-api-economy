"""Bangkitkan diagram konsep TikZ dari figures/chapter-diagrams.json.

Pemakaian dari akar repo: python tools/render-diagrams.py [--chapter 1 3]
Data yang diedit: figures/chapter-diagrams.json

Setiap bab menghasilkan figures/chNN-diagram-konsep.tex berisi satu tikzpicture
tanpa preamble, sehingga modul dan slide memakai gambar yang sama. Jalur panah
dicari dengan A* pada grid agar tidak menembus kotak, lalu label diletakkan
memakai metrik font Titillium Web dari module/fonts. Skrip hanya memakai pustaka
standar Python, sehingga tidak perlu matplotlib.
"""

from itertools import combinations
from operator import itemgetter
from pathlib import Path
import argparse
import heapq
import json
import struct


# Geometri grid sama dengan versi PNG sebelumnya supaya jalur panah tidak berubah.
GRID_STEP = 0.1
COLUMN_PITCH = 44
ROW_PITCH = 27
BOX_WIDTH = 3.26
BOX_HEIGHT = 1.4
PORT_REACH_X = 18
PORT_REACH_Y = 9
OBSTACLE_REACH_X = 17
OBSTACLE_REACH_Y = 8
ROUTE_LEFT = -25
ROUTE_RIGHT = 113
ROUTE_TOP = 19
ROUTE_BOTTOM_MARGIN = 20
BEND_COST = 3.5
SHARED_CELL_COST = 2.8
START_DIRECTION = 4
PORT_PAIRS_TRIED = 6
UNREACHABLE = 1e9
COLLINEAR_TOLERANCE = 1e-7
DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# Skala cetak: satu satuan diagram dalam cm. Lebar gambar sekitar 12 cm.
UNIT_X_CM = 0.92
UNIT_Y_CM = 0.95
POINTS_PER_CM = 72.27 / 2.54
POINTS_PER_UNIT_X = UNIT_X_CM * POINTS_PER_CM
POINTS_PER_UNIT_Y = UNIT_Y_CM * POINTS_PER_CM

# Ukuran font mengikuti \scriptsize dan \tiny pada kelas 11pt dan 12pt.
TITLE_SIZE_PT = 8
TITLE_LEADING_PT = 9.5
TITLE_CAP_HEIGHT_PT = 6
SUBTITLE_SIZE_PT = 6
SUBTITLE_LEADING_PT = 7.5
SUBTITLE_DEPTH_PT = 1.5
SUBTITLE_SHIFT_PT = SUBTITLE_LEADING_PT - TITLE_LEADING_PT
TITLE_TO_SUBTITLE_PT = 0.5
BOX_SIDE_MARGIN_PT = 3.5
BOX_VERTICAL_MARGIN_PT = 1.5
LABEL_SIZE_PT = 6
LABEL_LEADING_PT = 7
LABEL_INNER_SEP_PT = 1
LABEL_CLEARANCE_PT = 1.5
NOTE_GAP_CM = 0.35
# Lebar dari tabel hmtx sekitar 3 persen lebih sempit daripada hasil XeLaTeX.
WIDTH_SAFETY = 1.04

# Bobot penempatan label sama dengan versi PNG: kotak paling dihindari.
NODE_CLEARANCE = 0.08
LABEL_MIN_SEGMENT = 0.35
LABEL_MIN_WIDTH = 0.95
LABEL_MAX_WIDTH = 2.5
LABEL_WIDTH_SLACK = 0.08
LABEL_FRACTIONS = (0.5, 0.35, 0.65)
LABEL_GAP = 0.09
LABEL_SIDE_SHIFT = 0.25
LABEL_LEFT_LIMIT = -2.35
LABEL_RIGHT_LIMIT = 11.15
LABEL_TOP_LIMIT = 1.55
NODE_OVERLAP_WEIGHT = 200
LABEL_OVERLAP_WEIGHT = 90
BOUNDARY_WEIGHT = 100
SHORT_SEGMENT_WEIGHT = 2
OFFSET_WEIGHT = 0.1
LENGTH_WEIGHT = 0.03
CROSSING_PENALTY = 0.7
# Teks TikZ relatif lebih besar daripada PNG, jadi label boleh dibungkus lebih
# sempit. Label yang menutupi ujung panah atau pangkal garis diberi denda besar.
LABEL_WRAP_FACTORS = (1.0, 0.7, 0.45)
EXTRA_LINE_WEIGHT = 0.15
MIN_VISIBLE_STUB = 0.15
MIN_VISIBLE_ARROW = 0.32
COVER_WEIGHT = 10

# Warna per peran sama dengan PNG lama: isi muda dan garis tepi yang lebih tua.
ROLE_COLORS = {
  "actor": ("EEF1F6", "50627D"),
  "service": ("EAF2FB", "3F6893"),
  "control": ("E9F3EC", "316B4B"),
  "data": ("F1EDF8", "786394"),
  "outcome": ("E4F2EC", "236C57"),
  "risk": ("FCEDE7", "B36947"),
}
TEXT_COLORS = {
  "konsepJudul": "20394F",
  "konsepTeks": "455264",
  "konsepLabel": "35485C",
  "konsepPanah": "5C7084",
  "konsepPanahPutus": "A15D40",
}
LATEX_ESCAPES = {
  "\\": r"\textbackslash{}",
  "&": r"\&",
  "%": r"\%",
  "$": r"\$",
  "#": r"\#",
  "_": r"\_",
  "{": r"\{",
  "}": r"\}",
  "~": r"\textasciitilde{}",
  "^": r"\textasciicircum{}",
}


class FontMetrics:
  """Baca lebar glyph dari TTF agar pembungkusan teks mendekati hasil XeLaTeX."""

  def __init__(self, font_path):
    """Muat tabel head, hhea, hmtx, dan cmap; kerning diabaikan agar aman."""
    data = font_path.read_bytes()
    tables = font_tables(data)
    self.units_per_em = struct.unpack_from(">H", data, tables["head"] + 18)[0]
    metric_count = struct.unpack_from(">H", data, tables["hhea"] + 34)[0]
    metrics = struct.unpack_from(f">{2 * metric_count}H", data, tables["hmtx"])
    advances = metrics[0::2]
    glyphs = unicode_glyphs(data, tables["cmap"])
    self.advances = {
      code: advances[min(glyph, metric_count - 1)] for code, glyph in glyphs.items()
    }
    self.fallback = self.advances.get(ord("n"), self.units_per_em // 2)

  def width(self, text, size_pt):
    """Hitung lebar teks dalam poin TeX, dibulatkan ke atas mengikuti hasil XeLaTeX."""
    total = sum(self.advances.get(ord(character), self.fallback) for character in text)
    return total * size_pt / self.units_per_em * WIDTH_SAFETY


def font_tables(data):
  """Petakan nama tabel TTF ke posisi awalnya di dalam berkas."""
  table_count = struct.unpack_from(">H", data, 4)[0]
  offsets = {}
  for index in range(table_count):
    tag, _, offset, _ = struct.unpack_from(">4sIII", data, 12 + 16 * index)
    offsets[tag.decode("latin-1")] = offset
  return offsets


def unicode_glyphs(data, cmap_offset):
  """Ambil subtabel cmap Unicode format 4, yang dimiliki hampir semua font TTF."""
  subtable_count = struct.unpack_from(">H", data, cmap_offset + 2)[0]
  for index in range(subtable_count):
    platform, encoding, offset = struct.unpack_from(
      ">HHI", data, cmap_offset + 4 + 8 * index
    )
    start = cmap_offset + offset
    if (platform, encoding) == (3, 1) and struct.unpack_from(">H", data, start)[0] == 4:
      return format4_glyphs(data, start)
  raise ValueError("Font tidak memiliki cmap Unicode format 4.")


def format4_glyphs(data, start):
  """Uraikan segmen cmap format 4 menjadi peta kode karakter ke nomor glyph."""
  segment_count = struct.unpack_from(">H", data, start + 6)[0] // 2
  ends = struct.unpack_from(f">{segment_count}H", data, start + 14)
  arrays_start = start + 16
  unsigned, signed = f">{segment_count}H", f">{segment_count}h"
  starts = struct.unpack_from(unsigned, data, arrays_start + 2 * segment_count)
  deltas = struct.unpack_from(signed, data, arrays_start + 4 * segment_count)
  range_start = arrays_start + 6 * segment_count
  range_offsets = struct.unpack_from(f">{segment_count}H", data, range_start)
  glyphs = {}
  segments = zip(starts, ends, deltas, range_offsets)
  for segment, (first, last, delta, range_offset) in enumerate(segments):
    for code in range(first, min(last, 0xFFFE) + 1):
      if range_offset == 0:
        glyphs[code] = (code + delta) & 0xFFFF
        continue
      address = range_start + 2 * segment + range_offset + 2 * (code - first)
      glyph = struct.unpack_from(">H", data, address)[0]
      glyphs[code] = (glyph + delta) & 0xFFFF if glyph else 0
  return glyphs


def grid_position(node):
  """Ubah kolom dan baris JSON menjadi sel grid; baris bertambah ke bawah."""
  return (round(node["column"] * COLUMN_PITCH), round(-node["row"] * ROW_PITCH))


def blocked_cells(nodes):
  """Tandai sel di sekitar kotak agar jalur panah tidak menembus isi kotak."""
  blocked = set()
  for node in nodes:
    center_x, center_y = grid_position(node)
    for cell_x in range(center_x - OBSTACLE_REACH_X, center_x + OBSTACLE_REACH_X + 1):
      for cell_y in range(center_y - OBSTACLE_REACH_Y, center_y + OBSTACLE_REACH_Y + 1):
        blocked.add((cell_x, cell_y))
  return blocked


def node_ports(node):
  """Sediakan titik keluar tepat di luar sisi kanan, kiri, atas, dan bawah kotak."""
  center_x, center_y = grid_position(node)
  return [
    (center_x + PORT_REACH_X, center_y, "r"),
    (center_x - PORT_REACH_X, center_y, "l"),
    (center_x, center_y + PORT_REACH_Y, "t"),
    (center_x, center_y - PORT_REACH_Y, "b"),
  ]


def find_route(start, end, blocked, used, lowest_cell):
  """Cari jalur ortogonal termurah; belokan dan lajur bersama diberi biaya tambahan."""
  first = (start[0], start[1], START_DIRECTION)
  queue = [(0, 0, first)]
  costs = {first: 0}
  previous = {}
  goal = None
  while queue:
    _, cost, state = heapq.heappop(queue)
    cell_x, cell_y, direction = state
    if cost != costs[state]:
      continue
    if (cell_x, cell_y) == end:
      goal = state
      break
    for index, (step_x, step_y) in enumerate(DIRECTIONS):
      next_x, next_y = cell_x + step_x, cell_y + step_y
      if not ROUTE_LEFT <= next_x <= ROUTE_RIGHT:
        continue
      if not lowest_cell <= next_y <= ROUTE_TOP:
        continue
      if (next_x, next_y) in blocked:
        continue
      bend = 0 if direction in (START_DIRECTION, index) else BEND_COST
      crowding = used.get((next_x, next_y), 0) * SHARED_CELL_COST
      candidate = cost + 1 + bend + crowding
      neighbor = (next_x, next_y, index)
      if candidate < costs.get(neighbor, UNREACHABLE):
        costs[neighbor] = candidate
        previous[neighbor] = state
        estimate = abs(next_x - end[0]) + abs(next_y - end[1])
        heapq.heappush(queue, (candidate + estimate, candidate, neighbor))
  if goal is None:
    return None, UNREACHABLE
  path = []
  state = goal
  while state != first:
    path.append((state[0], state[1]))
    state = previous[state]
  path.append(start)
  return path[::-1], costs[goal]


def corner_points(path):
  """Simpan titik awal, titik belok, dan titik akhir saja."""
  result = [path[0]]
  for before, current, after in zip(path, path[1:], path[2:]):
    incoming = (current[0] - before[0], current[1] - before[1])
    outgoing = (after[0] - current[0], after[1] - current[1])
    if incoming != outgoing:
      result.append(current)
  result.append(path[-1])
  return result


def boundary_point(cell, side):
  """Geser titik keluar ke tepi kotak supaya garis menempel pada kotak."""
  reach_x = PORT_REACH_X * GRID_STEP - BOX_WIDTH / 2
  reach_y = PORT_REACH_Y * GRID_STEP - BOX_HEIGHT / 2
  shift = {"r": (-reach_x, 0), "l": (reach_x, 0), "t": (0, -reach_y), "b": (0, reach_y)}
  return (cell[0] * GRID_STEP + shift[side][0], cell[1] * GRID_STEP + shift[side][1])


def edge_span(nodes, edge):
  """Ukur jarak Manhattan antarkotak agar panah pendek dirutekan lebih dahulu."""
  source = grid_position(nodes[edge["source"]])
  target = grid_position(nodes[edge["target"]])
  return abs(source[0] - target[0]) + abs(source[1] - target[1])


def without_collinear(points):
  """Buang titik di tengah ruas lurus, termasuk penyambung pendek ke tepi kotak."""
  compact = [points[0]]
  for point in points[1:]:
    if len(compact) > 1:
      before, current = compact[-2:]
      cross = (current[0] - before[0]) * (point[1] - current[1]) - (
        current[1] - before[1]
      ) * (point[0] - current[0])
      if abs(cross) < COLLINEAR_TOLERANCE:
        compact[-1] = point
        continue
    compact.append(point)
  return compact


def route_edges(chapter):
  """Rutekan semua panah; panah pendek dahulu agar mendapat lajur langsung."""
  nodes = {node["id"]: node for node in chapter["nodes"]}
  blocked = blocked_cells(chapter["nodes"])
  used = {}
  lowest_row = max(node["row"] for node in chapter["nodes"])
  lowest_cell = -ROW_PITCH * lowest_row - ROUTE_BOTTOM_MARGIN
  ordered = sorted(
    (edge_span(nodes, edge), index, edge) for index, edge in enumerate(chapter["edges"])
  )
  routes = []
  for _, index, edge in ordered:
    candidates = []
    for source_port in node_ports(nodes[edge["source"]]):
      for target_port in node_ports(nodes[edge["target"]]):
        if edge.get("source_port") and source_port[2] != edge["source_port"]:
          continue
        if edge.get("target_port") and target_port[2] != edge["target_port"]:
          continue
        distance = abs(source_port[0] - target_port[0]) + abs(
          source_port[1] - target_port[1]
        )
        candidates.append((distance, source_port, target_port))
    candidates.sort(key=itemgetter(0))
    best = None
    for _, source_port, target_port in candidates[:PORT_PAIRS_TRIED]:
      path, cost = find_route(
        source_port[:2], target_port[:2], blocked, used, lowest_cell
      )
      if path and (best is None or cost < best[0]):
        best = (cost, path, source_port[2], target_port[2])
    if best is None:
      raise ValueError(f"Tidak ada jalur untuk panah {edge}")
    _, path, source_side, target_side = best
    for cell in path:
      used[cell] = used.get(cell, 0) + 1
    points = [(x * GRID_STEP, y * GRID_STEP) for x, y in corner_points(path)]
    points = (
      [boundary_point(path[0], source_side)]
      + points
      + [boundary_point(path[-1], target_side)]
    )
    routes.append((index, edge, without_collinear(points), source_side, target_side))
  return sorted(routes, key=itemgetter(0))


def wrap_words(text, metrics, size_pt, max_width_pt):
  """Bungkus kata ke baris seimbang; kata yang terlalu panjang tetap satu baris.

  Jumlah baris ditentukan pembungkusan rakus, lalu titik potong dipilih ulang
  supaya baris terpanjang sesempit mungkin. Teks rata tengah jadi tidak
  menyisakan satu kata pendek di baris terakhir.
  """
  greedy = []
  for word in text.split():
    if greedy and metrics.width(greedy[-1] + " " + word, size_pt) <= max_width_pt:
      greedy[-1] += " " + word
    else:
      greedy.append(word)
  words = text.split()
  best = None
  for breaks in combinations(range(1, len(words)), len(greedy) - 1):
    bounds = (0,) + breaks + (len(words),)
    lines = [" ".join(words[low:high]) for low, high in zip(bounds, bounds[1:])]
    widest = max(metrics.width(line, size_pt) for line in lines)
    if best is None or widest <= best[0]:
      best = (widest, lines)
  return best[1]


def rectangle_overlap(first, second):
  """Hitung luas irisan dua persegi panjang (kiri, bawah, kanan, atas)."""
  width = min(first[2], second[2]) - max(first[0], second[0])
  height = min(first[3], second[3]) - max(first[1], second[1])
  return max(0, width) * max(0, height)


def node_center(node):
  """Pusat kotak dalam satuan diagram."""
  cell_x, cell_y = grid_position(node)
  return (cell_x * GRID_STEP, cell_y * GRID_STEP)


def node_rectangles(nodes):
  """Daerah kotak plus jarak aman yang tidak boleh ditutup label."""
  rectangles = []
  for node in nodes:
    center_x, center_y = node_center(node)
    rectangles.append((
      center_x - BOX_WIDTH / 2 - NODE_CLEARANCE,
      center_y - BOX_HEIGHT / 2 - NODE_CLEARANCE,
      center_x + BOX_WIDTH / 2 + NODE_CLEARANCE,
      center_y + BOX_HEIGHT / 2 + NODE_CLEARANCE,
    ))
  return rectangles


def label_size(lines, metrics):
  """Ukuran kotak label dalam satuan diagram, termasuk jarak aman di sekelilingnya."""
  padding_pt = 2 * (LABEL_INNER_SEP_PT + LABEL_CLEARANCE_PT)
  text_width = max(metrics.width(line, LABEL_SIZE_PT) for line in lines)
  width = (text_width + padding_pt) / POINTS_PER_UNIT_X
  height = (len(lines) * LABEL_LEADING_PT + padding_pt) / POINTS_PER_UNIT_Y
  return width, height


def crossings(box, own_points, routes):
  """Hitung ruas panah lain yang tertutup kotak label."""
  count = 0
  for _, _, points, _, _ in routes:
    if points is own_points:
      continue
    for start, end in zip(points, points[1:]):
      if (
        min(start[0], end[0]) <= box[2]
        and max(start[0], end[0]) >= box[0]
        and min(start[1], end[1]) <= box[3]
        and max(start[1], end[1]) >= box[1]
      ):
        count += 1
  return count


def wrap_variants(label, max_width, metrics):
  """Siapkan beberapa cara membungkus label, dari satu baris sampai paling sempit."""
  variants = []
  for factor in LABEL_WRAP_FACTORS:
    width_pt = max_width * factor * POINTS_PER_UNIT_X
    lines = wrap_words(label, metrics, LABEL_SIZE_PT, width_pt)
    if lines not in variants:
      variants.append(lines)
  return variants


def label_choices(points, label, metrics):
  """Daftar posisi calon label di setiap ruas yang cukup panjang."""
  choices = []
  segment_count = len(points) - 1
  for index, (start, end) in enumerate(zip(points, points[1:])):
    length = abs(end[0] - start[0]) + abs(end[1] - start[1])
    horizontal = abs(end[1] - start[1]) < 1e-6
    if length < LABEL_MIN_SEGMENT:
      continue
    max_width = LABEL_MAX_WIDTH
    if horizontal:
      max_width = max(LABEL_MIN_WIDTH, min(LABEL_MAX_WIDTH, length - LABEL_WIDTH_SLACK))
    for lines in wrap_variants(label, max_width, metrics):
      width, height = label_size(lines, metrics)
      if horizontal:
        offsets = (height / 2 + LABEL_GAP, -height / 2 - LABEL_GAP, 0)
      else:
        offsets = (0, -LABEL_SIDE_SHIFT, LABEL_SIDE_SHIFT)
      for fraction in LABEL_FRACTIONS:
        for offset in offsets:
          x = start[0] + fraction * (end[0] - start[0])
          y = start[1] + fraction * (end[1] - start[1])
          if horizontal:
            y += offset
          else:
            x += offset
          segment = (start, end, index == segment_count - 1)
          choices.append((x, y, width, height, lines, offset, length, segment))
  return choices


def hidden_line(box, segment):
  """Ukur kekurangan garis yang masih terlihat di kedua ujung ruas di bawah label."""
  start, end, is_last = segment
  if abs(end[1] - start[1]) < 1e-6:
    crosses = box[1] <= start[1] <= box[3]
    low, high, first, last = box[0], box[2], start[0], end[0]
  else:
    crosses = box[0] <= start[0] <= box[2]
    low, high, first, last = box[1], box[3], start[1], end[1]
  if not crosses:
    return 0
  if last >= first:
    visible_start, visible_end = low - first, last - high
  else:
    visible_start, visible_end = first - high, low - last
  needed_end = MIN_VISIBLE_ARROW if is_last else MIN_VISIBLE_STUB
  return max(0, MIN_VISIBLE_STUB - visible_start) + max(0, needed_end - visible_end)


def place_label(points, label, occupied, rectangles, routes, metrics):
  """Pilih posisi label dengan skor tumpang tindih terkecil, seperti versi PNG."""
  best = None
  for choice in label_choices(points, label, metrics):
    x, y, width, height, lines, offset, length, segment = choice
    horizontal = abs(segment[1][1] - segment[0][1]) < 1e-6
    box = (x - width / 2, y - height / 2, x + width / 2, y + height / 2)
    node_overlap = sum(rectangle_overlap(box, other) for other in rectangles)
    label_overlap = sum(rectangle_overlap(box, other) for other in occupied)
    score = node_overlap * NODE_OVERLAP_WEIGHT + label_overlap * LABEL_OVERLAP_WEIGHT
    score += max(0, LABEL_LEFT_LIMIT - box[0]) * BOUNDARY_WEIGHT
    score += max(0, box[2] - LABEL_RIGHT_LIMIT) * BOUNDARY_WEIGHT
    score += max(0, box[3] - LABEL_TOP_LIMIT) * BOUNDARY_WEIGHT
    score += max(0, (width if horizontal else height) - length) * SHORT_SEGMENT_WEIGHT
    score += OFFSET_WEIGHT * abs(offset) + LENGTH_WEIGHT / length
    score += crossings(box, points, routes) * CROSSING_PENALTY
    score += hidden_line(box, segment) * COVER_WEIGHT
    score += (len(lines) - 1) * EXTRA_LINE_WEIGHT
    if best is None or score < best[0]:
      best = (score, x, y, box, lines)
  if best is None:
    raise ValueError(f"Label tidak mendapat ruas yang cukup panjang: {label}")
  _, x, y, box, lines = best
  occupied.append(box)
  return x, y, box, lines


def escape_latex(text):
  """Lindungi karakter khusus LaTeX seperti % dan _ dari teks JSON."""
  return "".join(LATEX_ESCAPES.get(character, character) for character in text)


def number(value):
  """Tulis koordinat dua desimal tanpa nol berlebih agar berkas mudah dibaca."""
  text = f"{value:.2f}".rstrip("0").rstrip(".")
  return "0" if text in ("-0", "") else text


def node_label(node, fonts):
  """Susun judul tebal dan subjudul kecil yang sudah dibungkus agar muat di kotak."""
  title, subtitle = node["text"].split("|")
  width_pt = BOX_WIDTH * POINTS_PER_UNIT_X - 2 * BOX_SIDE_MARGIN_PT
  title_lines = wrap_words(title, fonts["bold"], TITLE_SIZE_PT, width_pt)
  subtitle_lines = wrap_words(subtitle, fonts["regular"], SUBTITLE_SIZE_PT, width_pt)
  widest = max(
    [fonts["bold"].width(line, TITLE_SIZE_PT) for line in title_lines]
    + [fonts["regular"].width(line, SUBTITLE_SIZE_PT) for line in subtitle_lines]
  )
  if widest > width_pt:
    raise ValueError(f"Ada kata yang lebih lebar daripada kotak: {node['text']}")
  needed_pt = (
    TITLE_CAP_HEIGHT_PT
    + (len(title_lines) - 1) * TITLE_LEADING_PT
    + TITLE_LEADING_PT
    + TITLE_TO_SUBTITLE_PT
    + (len(subtitle_lines) - 1) * SUBTITLE_LEADING_PT
    + SUBTITLE_DEPTH_PT
  )
  available_pt = BOX_HEIGHT * POINTS_PER_UNIT_Y - 2 * BOX_VERTICAL_MARGIN_PT
  if needed_pt > available_pt:
    raise ValueError(f"Teks kotak terlalu panjang untuk tinggi kotak: {node['text']}")
  parts = [r"\textbf{" + escape_latex(line) + "}" for line in title_lines]
  text = r"\\".join(parts)
  text += f"\\\\[{number(TITLE_TO_SUBTITLE_PT)}pt]"
  subtitle_parts = [r"{\tiny\color{konsepTeks}" + escape_latex(line) + "}"
                    for line in subtitle_lines]
  text += f"\\\\[{number(SUBTITLE_SHIFT_PT)}pt]".join(subtitle_parts)
  return text


def picture_styles(box_width_cm, box_height_cm, note_width_cm):
  """Gaya bersama: kotak per peran, panah utuh, panah putus-putus, label, catatan."""
  lines = [
    r"\begin{tikzpicture}[",
    f"  x={number(UNIT_X_CM)}cm, y={number(UNIT_Y_CM)}cm,",
    "  kotak konsep/.style={draw, line width=0.5pt, rounded corners=2pt,",
    f"    align=center, minimum width={box_width_cm:.3f}cm,",
    f"    minimum height={box_height_cm:.3f}cm, inner sep=0pt, font=\\scriptsize,",
    "    text=konsepJudul},",
  ]
  for role in ROLE_COLORS:
    name = role.capitalize()
    lines.append(
      f"  peran {role}/.style={{kotak konsep, fill=konsepIsi{name}, "
      f"draw=konsepGaris{name}}},"
    )
  lines.extend([
    "  panah konsep/.style={-{Stealth[length=1.3mm, width=1.2mm]}, line width=0.6pt,",
    "    draw=konsepPanah},",
    "  panah putus/.style={panah konsep, draw=konsepPanahPutus,",
    "    dash pattern=on 2.5pt off 1.5pt},",
    "  label panah/.style={font=\\tiny, align=center, fill=white,",
    f"    inner sep={number(LABEL_INNER_SEP_PT)}pt, text=konsepLabel}},",
    "  catatan/.style={font=\\scriptsize, align=left, anchor=north west,",
    f"    inner sep=0pt, text width={note_width_cm:.3f}cm, text=konsepTeks,",
    "    execute at begin node={\\hyphenpenalty=10000\\hbadness=10000\\relax}},",
    "]",
  ])
  for role, (fill, line) in ROLE_COLORS.items():
    name = role.capitalize()
    lines.append(f"  \\definecolor{{konsepIsi{name}}}{{HTML}}{{{fill}}}")
    lines.append(f"  \\definecolor{{konsepGaris{name}}}{{HTML}}{{{line}}}")
  for name, value in TEXT_COLORS.items():
    lines.append(f"  \\definecolor{{{name}}}{{HTML}}{{{value}}}")
  return lines


def route_path(route):
  """Tulis jalur panah dengan koordinat mutlak; ujungnya tepat di tepi kotak."""
  _, edge, points, _, _ = route
  parts = [f"({number(x)},{number(y)})" for x, y in points]
  style = "panah putus" if edge.get("dashed") else "panah konsep"
  return f"  \\draw[{style}] " + " -- ".join(parts) + ";"


def check_label_text(label_box, label_lines, nodes):
  """Hentikan proses bila teks label, bukan sekadar latarnya, menimpa kotak."""
  padding_x = (LABEL_INNER_SEP_PT + LABEL_CLEARANCE_PT) / POINTS_PER_UNIT_X
  padding_y = (LABEL_INNER_SEP_PT + LABEL_CLEARANCE_PT) / POINTS_PER_UNIT_Y
  text_box = (
    label_box[0] + padding_x,
    label_box[1] + padding_y,
    label_box[2] - padding_x,
    label_box[3] - padding_y,
  )
  for node in nodes:
    center_x, center_y = node_center(node)
    box = (
      center_x - BOX_WIDTH / 2,
      center_y - BOX_HEIGHT / 2,
      center_x + BOX_WIDTH / 2,
      center_y + BOX_HEIGHT / 2,
    )
    if rectangle_overlap(text_box, box) > 0:
      label = " ".join(label_lines)
      raise ValueError(
        f"Label '{label}' menimpa kotak '{node['id']}'; perpendek label."
      )


def tikz_picture(chapter, fonts):
  """Bangun isi berkas .tex untuk satu bab dari spesifikasi JSON-nya."""
  nodes = chapter["nodes"]
  routes = route_edges(chapter)
  rectangles = node_rectangles(nodes)
  occupied = []
  labels = []
  for route in routes:
    _, edge, points, _, _ = route
    labels.append(
      place_label(points, edge["label"], occupied, rectangles, routes, fonts["regular"])
    )
  centers = [node_center(node) for node in nodes]
  left = min(x for x, _ in centers) - BOX_WIDTH / 2
  right = max(x for x, _ in centers) + BOX_WIDTH / 2
  lowest = min(y for _, y in centers) - BOX_HEIGHT / 2
  lowest = min([lowest] + [y for route in routes for _, y in route[2]])
  lowest = min([lowest] + [box[1] for _, _, box, _ in labels])
  note_top = lowest - NOTE_GAP_CM / UNIT_Y_CM
  lines = [
    f"% Diagram konsep Bab {chapter['number']}: {chapter['caption']}.",
    "% Dibangkitkan tools/render-diagrams.py dari figures/chapter-diagrams.json;",
    "% ubah data JSON lalu jalankan ulang skrip, jangan sunting berkas ini langsung.",
  ]
  lines.extend(picture_styles(
    BOX_WIDTH * UNIT_X_CM, BOX_HEIGHT * UNIT_Y_CM, (right - left) * UNIT_X_CM
  ))
  lines.append("  % Panah dan label lebih dahulu; kotak menutupi sisa latar label.")
  for route in routes:
    lines.append(route_path(route))
  for x, y, box, label_lines in labels:
    check_label_text(box, label_lines, nodes)
    text = r"\\".join(escape_latex(line) for line in label_lines)
    lines.append(f"  \\node[label panah] at ({number(x)},{number(y)}) {{{text}}};")
  for node, (x, y) in zip(nodes, centers):
    lines.append(
      f"  \\node[peran {node['role']}] ({node['id']}) at ({number(x)},{number(y)})"
    )
    lines.append(f"    {{{node_label(node, fonts)}}};")
  lines.append(
    f"  \\node[catatan] at ({number(left)},{number(note_top)})"
  )
  lines.append(f"    {{{escape_latex(chapter['note'])}}};")
  lines.append(r"\end{tikzpicture}")
  return "\n".join(lines) + "\n"


def main():
  """Tulis satu berkas TikZ per bab; pilih bab tertentu dengan --chapter."""
  parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
  parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[1])
  parser.add_argument("--chapter", type=int, nargs="*")
  args = parser.parse_args()
  specs = json.loads(
    (args.repo / "figures/chapter-diagrams.json").read_text(encoding="utf-8")
  )
  font_folder = args.repo / "module/fonts"
  fonts = {
    "regular": FontMetrics(font_folder / "TitilliumWeb-Regular.ttf"),
    "bold": FontMetrics(font_folder / "TitilliumWeb-Bold.ttf"),
  }
  for chapter in specs["chapters"]:
    if args.chapter and chapter["number"] not in args.chapter:
      continue
    destination = args.repo / "figures" / Path(chapter["filename"]).with_suffix(".tex")
    destination.write_text(tikz_picture(chapter, fonts), encoding="utf-8")
    print(destination.name, flush=True)


if __name__ == "__main__":
  main()
