# Plan

## Next steps to decide
1) Confirm hot-swap socket part
   - Decision: generic Kailh Choc hot-swap socket footprint (same for Choc v1/v2).

2) Choose stabilizers
   - Low-profile plate-mount stabilizers for 2u and 6.25u positions.
   - Confirm brand/model and whether any PCB-mount support is needed.
   - Decision: plate-mount Choc stabilizers (4x 2u, 1x 6.25u).

3) Choose battery
   - Pick thickness target (3 mm / 4 mm / 5 mm), capacity, and connector type.
   - Verify the nice!nano clone battery connector (JST-PH 2.0 vs JST-1.25).
   - Decision: 4 mm thickness, JST-PH.

4) Confirm keycap strategy
   - Decide whether to keep standard-height caps or switch to low-profile caps for a thinner feel.
   - Decision: low-profile, 8–9 mm height.

5) Define ZMK layer behavior
   - Decision: Fn+Device 1/2/3 macro for re-pair (BT_SEL N -> BT_CLR -> BT_SEL N; avoid BT_CLR_ALL).

6) Decide backlight implementation
   - Choose LED type and placement (per-key vs edge-lit light guide).
   - Decision: 1 mm clear plate as edge-lit light guide with up to 16 side-emitting white LEDs, single PWM zone.
   - Pick side-emitting LED part (1206) and warm/neutral color temperature based on availability.

7) Decide switch/IO details
   - External power switch placement.
   - Decision: reset/boot access onboard only.
   - Decision: edge-mounted slide switch.

8) Begin design artifacts
   - Build ANSI TKL layout in KLE.
   - Import into KiCad, create schematic (matrix + diodes + nice!nano + power) and PCB.
   - Add BLE antenna keep-out and board outline for custom case.
