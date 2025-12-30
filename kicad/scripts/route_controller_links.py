import pcbnew


# Helper to connect row/column buses to the controller/expander.

TRACK_WIDTH_MM = 0.25
ROW_LAYER = pcbnew.F_Cu
COL_LAYER = pcbnew.B_Cu
ROW_PREFIX = "ROW"
COL_PREFIX = "COL"
ROW_COUNT = 8
COL_COUNT = 16


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


def _pad_for_net(board, net_name, ref_prefix):
    pads = _pads_for_net(board, net_name, ref_prefixes=(ref_prefix,))
    return pads[0] if pads else None


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


def connect_rows(board):
    width = _track_width(board)
    for idx in range(ROW_COUNT):
        net_name = f"{ROW_PREFIX}{idx}"
        u1_pad = _pad_for_net(board, net_name, "U1")
        if not u1_pad:
            continue
        diode_pads = _pads_for_net(board, net_name, ref_prefixes=("D",))
        if not diode_pads:
            continue
        target = min(diode_pads, key=lambda p: abs(p.GetPosition().x - u1_pad.GetPosition().x))
        u1_pos = u1_pad.GetPosition()
        target_pos = target.GetPosition()
        elbow = pcbnew.VECTOR2I(u1_pos.x, target_pos.y)
        _add_track(board, u1_pos, elbow, u1_pad.GetNetCode(), ROW_LAYER, width)
        _add_track(board, elbow, target_pos, u1_pad.GetNetCode(), ROW_LAYER, width)


def connect_cols(board):
    width = _track_width(board)
    for idx in range(COL_COUNT):
        net_name = f"{COL_PREFIX}{idx}"
        u2_pad = _pad_for_net(board, net_name, "U2")
        if not u2_pad:
            continue
        sw_pads = _pads_for_net(board, net_name, ref_prefixes=("SW",))
        if not sw_pads:
            continue
        spine_x = int(sum(pad.GetPosition().x for pad in sw_pads) / len(sw_pads))
        u2_pos = u2_pad.GetPosition()
        spine_point = pcbnew.VECTOR2I(spine_x, u2_pos.y)
        _add_track(board, u2_pos, spine_point, u2_pad.GetNetCode(), COL_LAYER, width)


def main():
    board = pcbnew.GetBoard()
    if not board.GetFileName():
        raise RuntimeError("Board is not saved yet. Save the PCB and rerun.")
    connect_rows(board)
    connect_cols(board)
    pcbnew.Refresh()
    print("Connected rows to U1 and columns to U2.")


if __name__ == "__main__":
    main()
