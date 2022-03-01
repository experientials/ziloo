The development board uses a single Expander. The 909 and 801 uses 3x PCA9555 to control more states.

The EX1 expander input triggers interrupt via EX_OH_nINT (GPIO1_IO0).
The pins relate to USB1 OTG and M.2 Key E.

The EX1 expander allows controlling T-USB maps,

The 3 pins for each Alt. Mode controller determines how signals are mapped to USB-C high speed lines.
Refer to the datasheet for HD3SS460 for full truth table. The regular USBSS setup is chosen by POL=L, AMSEL=M, EN=H.


| Expander  | Connected to    |
|-----------|-----------------|
| EX1.0     | USB_O_ALT_EN    |
| EX1.1     | USB_O_ALT_POL   |
| EX1.2     | USB_O_ALT_AMSEL |
| EX1.3     | MUX_USB2_SEL    |
| EX1.4     | MUX_USB3_SEL   |
| EX1.5     | COEX4 |
| EX1.6     | DEV_WLAN_WAKE      |
| EX1.7     | ALERT / I2C_IRQ    |
| EX1.8     | GPIO3 on 65988 (HPD1) |
| EX1.9     | LED / DAS / DSS  |
| EX1.10    | W_DISABLE2#                |
| EX1.11    | W_DISABLE1#                |
| EX1.12    | UART WAKE                |
| EX1.13    | SDIO WAKE                |
| EX1.14    | LED2#                |
| EX1.15    |                 |





