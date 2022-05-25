
This EX3 Combined T-USB control I/O Expander is placed on T-USB daughterboard and controlled via the Stem I2C.

The EX3 expander input triggers interrupt via STEM_INT.
The pins relate to USB1 OTG, USB2 Host, PD Controller

The EX3 expander allows controlling T-USB maps,

The 3 pins for each Alt. Mode controller determines how signals are mapped to USB-C high speed lines.
The regular USBSS setup is chosen by POL=L, AMSEL=M, EN=H.

| Expander  | Connected to    |
|-----------|-----------------|
| EX3.0     | PD_CTL_INT_1    |
| EX3.1     | PD_CTL_INT_2     |
| EX3.2     | PD_CTL_RESET     |
| EX3.3     | T_USB_O_ALT_EN    |
| EX3.4     | T_USB_O_ALT_POL  |
| EX3.5     | T_USB_O_ALT_AMSEL |
| EX3.6     | T_USB_H_ALT_EN     |
| EX3.7     | T_USB_H_ALT_POL   |
| EX3.8     | T_USB_H_ALT_AMSEL |
| EX3.9     | T_USB_ALERT    |
| EX3.10    | BAT_CE    |
| EX3.11    | BAT_INT            |
| EX3.12    | OHX_MODE_BIT_0   |
| EX3.13    | OHX_MODE_BIT_1   |
| EX3.14    | Select OTG Extra A6/A7 (OXA_SEL)  |
| EX3.15    | Select OTG Extra B6/B7 (OXB_SEL)  |


OTG and Host USB 2.0 connectivity options.
2 bit switching of USB 2.0 mode.
It may be combined with Alt Modes to be 3 bit.

| OHX MODE  | Signal combination |
|-----------|--------------------|
| 0         | Regular USB 2.0 data on USB1/USB2 A/B |
| 1         | USB1 A=Regular, B=Debug UARTs. USB2 3.0 Alt mode = JTAG


No outlet:

| EX1.8     | GPIO3 on 65988 (HPD1) |
| EX2.8     | GPIO4 on 65988 (HPD2) |




