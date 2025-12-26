# TKL Low-Profile Bluetooth Keyboard (Project Notes)

## Decisions so far
- Layout: ANSI TKL (87-key).
- Switches: Kailh Deep Sea Silent Mini Low-Profile (Kailh page indicates Choc v2 family / PG1353).
- Footprint target: Choc v2 (not Cherry MX pin layout, not Choc v1 keycaps).
- Stem: MX-style "+" stem (per Choc v2 description).
- Hot-swap: required.
- Controller: nice!nano v2-compatible BLE clones (same pinout as nice!nano v2).
- Features: no rotary encoder, no OLED; RGB/underglow undecided but likely skipped for thinness.
- Case: custom, as thin as possible.

## Findings / constraints
- Kailh product note: these switches are not compatible with Cherry MX key pin layouts and not compatible with Choc v1 keycaps.
- Beekeeb Choc v2 page: Choc v2 uses the same hot-swap sockets as Choc v1.
- Thin build drivers: battery thickness, PCB thickness, and component height will dominate overall thickness.

## Open decisions
- Hot-swap socket part number (confirm the exact Kailh Choc socket used).
- Stabilizers (low-profile plate-mount vs PCB-mount; sizes needed for TKL).
- Battery size and connector (thickness target, capacity, and JST type on the clone boards).
- Keycap profile suitability for low-profile build (current set may be standard-height).

