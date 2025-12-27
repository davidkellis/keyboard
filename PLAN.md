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
   - Decision: switch on the back edge.

8) Confirm matrix I/O strategy
   - Decision: use MCP23017 at 0x20 with 8x16 matrix.
   - Decision: row/column pin assignment set in hardware/matrix_plan.md.

9) Begin design artifacts
   - Build ANSI TKL layout in KLE.
     - Done: layout/ansi_tkl_device_keys.kle.json.
   - Draft schematic plan for KiCad.
     - Done: hardware/schematic_plan.md.
   - Create initial KiCad project files.
     - Done: kicad/tkl_low_profile.kicad_pro
     - Done: kicad/tkl_low_profile.kicad_sch
     - Done: kicad/tkl_low_profile.kicad_pcb
   - Vendor ScottoKicad libraries and add project library tables.
     - Done: kicad/lib/ScottoKicad
     - Done: kicad/fp-lib-table
     - Done: kicad/sym-lib-table
   - Generate matrix-annotated layout + switch/diode schematic.
     - Done: layout/ansi_tkl_device_keys.matrix.json
     - Done: kicad/tkl_low_profile.kicad_sch
     - Done: hardware/matrix_map.csv
   - Add core components to schematic (nice!nano, MCP23017, power, backlight placeholders).
     - Done: kicad/tkl_low_profile.kicad_sch
   - Wire the schematic (rows/cols, I2C, power, backlight nets).
   - Add BLE antenna keep-out and board outline for custom case.


• I proceeded by generating the switch/diode matrix schematic from the KLE, then injecting the core electronics symbols into the schematic so the project can move into
  wiring and PCB layout.

  What’s in place now

  - Switch/diode matrix schematic from the annotated KLE in kicad/tkl_low_profile.kicad_sch.
  - Extra symbols placed in the schematic for nice!nano (U1), MCP23017 (U2), battery connector, power switch, backlight MOSFET, pull‑ups, decoupling, and 16 LED/
    resistor placeholders.
  - Matrix map exported at hardware/matrix_map.csv and updated plan/docs.

  Key files

  - kicad/tkl_low_profile.kicad_sch
  - layout/ansi_tkl_device_keys.matrix.json
  - hardware/matrix_map.csv
  - hardware/matrix_plan.md
  - hardware/schematic_plan.md

  Important note

  - The new symbols are placed but not wired yet (no net labels or wires). The schematic is ready for wiring, then PCB update.

  If you want me to continue, I can:

  1. Wire the schematic (ROW/COL nets, I2C, power switch + battery, backlight MOSFET + LED rails).
  2. Update the PCB from the schematic.
  3. Place switch footprints using the KLE mapping and start routing.

  Say “continue wiring” and I’ll move on to step 1.
