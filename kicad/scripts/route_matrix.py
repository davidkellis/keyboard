import pcbnew


# Simple autoroute helper for row/column buses.
# It draws straight segments between adjacent pads for each net.

TRACK_WIDTH_MM = 0.25
ROW_LAYER = pcbnew.F_Cu
COL_LAYER = pcbnew.B_Cu
ROW_PREFIX = "ROW"
COL_PREFIX = "COL"
ROW_COUNT = 8
COL_COUNT = 16

# Routing toggles.
ROUTE_ROWS = True
ROUTE_COLS = True
COL_STYLE = "spine"  # "spine" or "chain"


def _from_mm(mm):
    return pcbnew.FromMM(mm)


def _track_width(board):
    settings = board.GetDesignSettings()
    width = None
    if hasattr(settings, "GetTrackWidth"):
        width = settings.GetTrackWidth()
    elif hasattr(settings, "GetCurrentTrackWidth"):
        width = settings.GetCurrentTrackWidth()
    elif hasattr(settings, "GetTrackWidthList") and hasattr(settings, "GetTrackWidthIndex"):
        widths = settings.GetTrackWidthList()
        idx = settings.GetTrackWidthIndex()
        if widths and 0 <= idx < len(widths):
            width = widths[idx]
    if not width or width <= 0:
        return _from_mm(TRACK_WIDTH_MM)
    return width


def _pads_for_net(board, net_name, ref_prefixes=None):
    pads = []
    for fp in board.GetFootprints():
        ref = fp.GetReference()
        if ref_prefixes and not ref.startswith(ref_prefixes):
            continue
        for pad in fp.Pads():
            net = pad.GetNet()
            if net and net.GetNetname() == net_name:
                pads.append(pad)
    return pads


def _add_track(board, start, end, net_code, layer, width):
    if hasattr(pcbnew, "PCB_TRACK"):
        track = pcbnew.PCB_TRACK(board)
    else:
        track = pcbnew.TRACK(board)
    track.SetStart(start)
    track.SetEnd(end)
    track.SetLayer(layer)
    track.SetNetCode(net_code)
    track.SetWidth(width)
    board.Add(track)


def _route_net(board, net_name, pads, layer, width, sort_key):
    if len(pads) < 2:
        return
    pads_sorted = sorted(pads, key=sort_key)
    for prev, curr in zip(pads_sorted, pads_sorted[1:]):
        start = prev.GetPosition()
        end = curr.GetPosition()
        _add_track(board, start, end, prev.GetNetCode(), layer, width)


def route_rows(board):
    width = _track_width(board)
    for idx in range(ROW_COUNT):
        net_name = f"{ROW_PREFIX}{idx}"
        pads = _pads_for_net(board, net_name, ref_prefixes=("D",))
        _route_net(board, net_name, pads, ROW_LAYER, width, sort_key=lambda p: p.GetPosition().x)

def _route_cols_chain(board):
    width = _track_width(board)
    for idx in range(COL_COUNT):
        net_name = f"{COL_PREFIX}{idx}"
        pads = _pads_for_net(board, net_name, ref_prefixes=("SW",))
        _route_net(board, net_name, pads, COL_LAYER, width, sort_key=lambda p: p.GetPosition().y)


def _route_cols_spine(board):
    width = _track_width(board)
    for idx in range(COL_COUNT):
        net_name = f"{COL_PREFIX}{idx}"
        pads = _pads_for_net(board, net_name, ref_prefixes=("SW",))
        if len(pads) < 2:
            continue
        xs = [pad.GetPosition().x for pad in pads]
        ys = [pad.GetPosition().y for pad in pads]
        spine_x = int(sum(xs) / len(xs))
        min_y = min(ys)
        max_y = max(ys)
        start = pcbnew.VECTOR2I(spine_x, min_y)
        end = pcbnew.VECTOR2I(spine_x, max_y)
        _add_track(board, start, end, pads[0].GetNetCode(), COL_LAYER, width)
        for pad in pads:
            pos = pad.GetPosition()
            if pos.x == spine_x:
                continue
            spine_point = pcbnew.VECTOR2I(spine_x, pos.y)
            _add_track(board, pos, spine_point, pad.GetNetCode(), COL_LAYER, width)


def route_cols(board):
    if COL_STYLE == "spine":
        _route_cols_spine(board)
    else:
        _route_cols_chain(board)


def main():
    board = pcbnew.GetBoard()
    if not board.GetFileName():
        raise RuntimeError("Board is not saved yet. Save the PCB and rerun.")
    if ROUTE_ROWS:
        route_rows(board)
    if ROUTE_COLS:
        route_cols(board)
    pcbnew.Refresh()
    print("Routed guide tracks.")


if __name__ == "__main__":
    main()
