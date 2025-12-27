# Schematic Plan (Draft)

## MCU / Module
- nice!nano v2-compatible (Pro Micro footprint).
- BLE antenna keep-out noted on PCB outline.

## Matrix
- 8x16 matrix, row-to-column diode direction.
- Rows on nice!nano:
  - ROW0: D4  (P0.22)
  - ROW1: D5  (P0.24)
  - ROW2: D6  (P1.00)
  - ROW3: D7  (P0.11)
  - ROW4: D8  (P1.04)
  - ROW5: D9  (P1.06)
  - ROW6: D16 (P0.10)
  - ROW7: D14 (P1.11)
- Columns on MCP23017 @ 0x20:
  - COL0-7:  GPA0-7
  - COL8-15: GPB0-7

## MCP23017 (I2C expander)
- VDD: 3.3V (VCC), GND.
- A0/A1/A2: GND (address 0x20).
- /RESET: pull-up to VDD (10k) + optional reset pad.
- I2C: D2 (SDA) + D3 (SCL).
- I2C pull-ups: 4.7k to 3.3V.
- Decoupling: 0.1uF near VDD.

## Backlight (single zone, PWM)
- Side-emitting 1206 LEDs around plate perimeter (up to 16).
- Supply: 3.3V (VCC) to reduce brightness variance on battery.
- Low-side N-MOSFET switch driven by D10 (P0.09).
- Gate resistor + pulldown to keep LEDs off on boot.
- LED current limiting: individual resistors per LED or per small group,
  value to be chosen after LED Vf is known (target low brightness).

## Power
- JST-PH battery connector.
- Edge-mounted slide switch on back-right edge, in series with battery positive
  to the nice!nano BAT/VBATT pin.

## Notes
- ZMK config: enable `kscan-gpio-matrix` + MCP23017 driver + backlight PWM.
- Schematic currently has placed symbols but wiring and net labels are still pending.
