# TKL Low-Profile Bluetooth Keyboard (Project Notes)

## Decisions so far
- Layout: ANSI TKL (87-key).
- Switches: Kailh Deep Sea Silent Mini Low-Profile (Kailh page indicates Choc v2 family / PG1353).
- Footprint target: Choc v2 (not Cherry MX pin layout, not Choc v1 keycaps).
- Stem: MX-style "+" stem (per Choc v2 description).
- Hot-swap: required.
- Switch footprints: MX_V2 Kailh PG1353 hotswap library (Kailh_PG1353_Hotswap).
- Controller: nice!nano v2-compatible BLE clones (same pinout as nice!nano v2).
- Features: no rotary encoder, no OLED; white backlight via edge-lit plate.
- Case: custom, as thin as possible.
- Firmware: ZMK.
- Fn layer: right Menu key.
- Device switching: map Device 1/2/3 to the three keys right of F12 (Print/Scroll/Pause positions).
- Keymap change: Insert key performs Print Screen.
- Re-pair: Fn+Device 1/2/3 macros force-select profile 0/1/2, clear bond (BT_CLR), then re-select that profile to enter pairing; avoids BT_CLR_ALL. Order: BT_SEL N -> BT_CLR -> BT_SEL N.
- Device select: tap Device 1/2/3 selects and connects to profile 0/1/2.
- Battery: 4 mm thickness, JST-PH.
- Keycaps: low-profile, 8–9 mm height.
- Stabilizers: Kailh Choc low-profile plate-mount (4x 2u, 1x 6.25u).
- Backlight: single-zone white; use 1 mm clear plate as the edge-lit light guide with up to 16 side-emitting 1206 LEDs around the perimeter; warm/neutral based on LED availability.
- External power switch: yes, edge-mounted slide switch on the back edge (back-right).
- Reset/boot access: onboard only.
- Matrix: 8x16; rows on nice!nano (D4-D9, D16, D14) and columns on MCP23017.
- MCP23017 I2C address: 0x20 (A0-A2 tied to GND).
- PCB thickness: 1.2 mm (initial assumption for thin build).
- KiCad libraries: ScottoKicad vendored at kicad/lib/ScottoKicad.

## Findings / constraints
- Kailh product note: these switches are not compatible with Cherry MX key pin layouts and not compatible with Choc v1 keycaps.
- Beekeeb Choc v2 page: Choc v2 uses the same hot-swap sockets as Choc v1.
- Thin build drivers: battery thickness, PCB thickness, and component height will dominate overall thickness.

## Open decisions
- Warm vs neutral LED selection based on availability.
- LED part selection based on availability (side-emitting 1206, warm/neutral).
- Side-emitting LED footprint (current schematic uses generic 1206 placeholder).
