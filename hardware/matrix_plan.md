# Matrix Plan

## Why an expander is likely needed
A full ANSI TKL layout (87 keys) does not fit on the 18 GPIO pins exposed by the
nice!nano v2 Pro Micro footprint once you reserve at least one pin for the
PWM backlight. A simple diode matrix needs more I/O than the module exposes.

## Matrix size
- Use an 8 row x 16 column matrix (128 key capacity).
- Rows on the nice!nano GPIOs (8 pins).
- Columns on an I2C GPIO expander (all 16 pins).
- I2C uses D2/D3 (P0.17/P0.20) on the nice!nano.

## Expander
- MCP23017 (16-bit I2C GPIO expander).
- ZMK supports MCP23017 (used in the Ferris board), so kscan-gpio-matrix can
  reference its GPIOs in devicetree.
- Use all 16 columns.

## Pin assignments (proposed)
### Rows (nice!nano)
- ROW0: D4  (P0.22)
- ROW1: D5  (P0.24)
- ROW2: D6  (P1.00)
- ROW3: D7  (P0.11)
- ROW4: D8  (P1.04)
- ROW5: D9  (P1.06)
- ROW6: D16 (P0.10)
- ROW7: D14 (P1.11)

### Columns (MCP23017 @ 0x20)
- COL0:  GPA0
- COL1:  GPA1
- COL2:  GPA2
- COL3:  GPA3
- COL4:  GPA4
- COL5:  GPA5
- COL6:  GPA6
- COL7:  GPA7
- COL8:  GPB0
- COL9:  GPB1
- COL10: GPB2
- COL11: GPB3
- COL12: GPB4
- COL13: GPB5
- COL14: GPB6
- COL15: GPB7

### Other reserved pins
- I2C: D2 (P0.17) SDA, D3 (P0.20) SCL
- Backlight PWM: D10 (P0.09)

## Diode direction
- Row-to-column.

## Column mapping approach
- Columns are assigned left-to-right within each row (ROW0..ROW7) to avoid
  conflicts; column indices do not strictly follow physical X alignment.

## Reference
- See hardware/matrix_map.csv for the current key-to-row/col mapping.
