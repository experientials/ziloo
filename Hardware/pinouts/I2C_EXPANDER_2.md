The development board uses a single Expander. The 909 and 801 uses 3x PCA9555 to control more states.

The EX2 expander input triggers interrupt via EX_H_nINT (GPIO1_IO0).
The pins relate to USB2 Host and M.2 Key B.

The EX2 expander allows controlling T-USB maps,

| Expander  | Connected to    |
|-----------|-----------------|
| EX2.0     | USB_H_ALT_EN    |
| EX2.1     | USB_H_ALT_POL   |
| EX2.2     | USB_H_ALT_AMSEL |
| EX2.3     | MUX_USB2_SEL    |
| EX2.4     | MUX_USB3_SEL   |
| EX2.5     | M2B_PWROFF |
| EX2.6     | RESET#      |
| EX2.7     | ALERT / I2C_IRQ    |
| EX2.8     | GPIO4 on 65988 (HPD2) |
| EX2.9     | GPIO9 / LED / DAS / DSS                |
| EX2.10    | GPIO10 / W_DISABLE_2#                |
| EX2.11    | W_DISABLE#                |
| EX2.12    | DEVSLP 3V3                |
| EX2.13    |                 |
| EX2.14    | CONFIG_1                |
| EX2.15    |                 |



