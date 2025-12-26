# Plan

## Next steps to decide
1) Confirm hot-swap socket part
   - Likely Kailh Choc hot-swap socket (same for Choc v1/v2). Confirm exact footprint or part number.

2) Choose stabilizers
   - Low-profile plate-mount stabilizers for 2u and 6.25u positions.
   - Confirm brand/model and whether any PCB-mount support is needed.

3) Choose battery
   - Pick thickness target (3 mm / 4 mm / 5 mm), capacity, and connector type.
   - Verify the nice!nano clone battery connector (JST-PH 2.0 vs JST-1.25).

4) Confirm keycap strategy
   - Decide whether to keep standard-height caps or switch to low-profile caps for a thinner feel.

5) Begin design artifacts
   - Build ANSI TKL layout in KLE.
   - Import into KiCad, create schematic (matrix + diodes + nice!nano + power) and PCB.
   - Add BLE antenna keep-out and board outline for custom case.

• Great — with nice!nano v2 pinout confirmed and Choc v2 switches, the parts list is straightforward.

  Hot‑swap sockets

  - Use the standard Kailh Choc hot‑swap sockets. Choc v2 uses the same sockets as Choc v1 (per the beekeeb Choc v2 page).
  - These are the common 2‑pin SMD Choc sockets used in most low‑profile builds and have well‑known KiCad footprints.

  Stabilizers (for ANSI TKL)

  - Use Kailh Choc low‑profile stabilizers, plate‑mount.
  - You’ll need: 4x 2u (Backspace, Enter, LShift, RShift) + 1x 6.25u for the spacebar.
  - Plate‑mount keeps the build thinner than PCB‑mount.

  Battery (thin build, nice!nano)

  - 3.7V LiPo with JST‑PH 2‑pin (please confirm your clone uses JST‑PH and not JST‑1.25).
  - Thin option: 3.0–3.5 mm thick cells, ~200–400 mAh depending on size.
  - Longer life: 4–5 mm thick cells, ~500–1000 mAh depending on size.
  - We’ll place it away from the BLE antenna keep‑out and usually under the spacebar area.

  Before I start the KiCad project, please pick:

  1. Battery thickness target (3 mm / 4 mm / 5 mm)
  2. Stabilizer type: Kailh Choc plate‑mount ok?
  3. Confirm your nice!nano clone battery connector type (JST‑PH 2.0 or something else)

  Once you confirm those, I’ll set up the schematic + PCB layout for the ANSI TKL Choc v2 hot‑swap board.

