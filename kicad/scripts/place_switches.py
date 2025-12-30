import csv
import pathlib

import pcbnew


# Placement settings.
U_MM = 19.05
ORIGIN_X_MM = 20.0
ORIGIN_Y_MM = 20.0
ROTATION_DEG = 0.0
FLIP_X = False
FLIP_Y = False


def _from_mm(mm):
    return pcbnew.FromMM(mm)


def _board_paths(board):
    board_path = pathlib.Path(board.GetFileName())
    if not board_path.name:
        raise RuntimeError("Board is not saved yet. Save the PCB and rerun.")
    root = board_path.parent.parent
    return board_path, root


def _load_matrix_map(map_path):
    with map_path.open(newline="") as handle:
        reader = csv.DictReader(handle)
        rows = list(reader)
    if not rows:
        raise RuntimeError("matrix_map.csv is empty.")
    return rows


def _switch_footprints(board):
    switches = {}
    for fp in board.GetFootprints():
        ref = fp.GetReference()
        if ref.startswith("SW") and ref[2:].isdigit():
            switches[int(ref[2:])] = fp
    return switches


def _place_switches(board, rows):
    xs = []
    ys = []
    for row in rows:
        x = float(row["x"])
        y = float(row["y"])
        w = float(row.get("w", 1.0))
        h = float(row.get("h", 1.0))
        xs.append(x + (w / 2.0))
        ys.append(y + (h / 2.0))
    min_x = min(xs)
    max_x = max(xs)
    min_y = min(ys)
    max_y = max(ys)

    switches = _switch_footprints(board)
    if not switches:
        raise RuntimeError("No SW* footprints found on the board.")

    for idx, row in enumerate(rows, start=1):
        fp = switches.get(idx)
        if fp is None:
            raise RuntimeError(f"Missing footprint SW{idx}.")

        x = float(row["x"])
        y = float(row["y"])
        w = float(row.get("w", 1.0))
        h = float(row.get("h", 1.0))
        center_x = x + (w / 2.0)
        center_y = y + (h / 2.0)
        x_u = (max_x - center_x) if FLIP_X else (center_x - min_x)
        y_u = (max_y - center_y) if FLIP_Y else (center_y - min_y)

        x_mm = ORIGIN_X_MM + (x_u * U_MM)
        y_mm = ORIGIN_Y_MM + (y_u * U_MM)

        fp.SetPosition(pcbnew.VECTOR2I(_from_mm(x_mm), _from_mm(y_mm)))
        fp.SetOrientationDegrees(ROTATION_DEG)


def main():
    board = pcbnew.GetBoard()
    _board_paths(board)  # Ensures the board is saved.
    _, root = _board_paths(board)
    map_path = root / "hardware" / "matrix_map.csv"
    rows = _load_matrix_map(map_path)
    _place_switches(board, rows)
    pcbnew.Refresh()
    print("Placed switch footprints from matrix_map.csv.")


if __name__ == "__main__":
    main()
