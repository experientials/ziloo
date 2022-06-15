
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
| EX3.12    | Select Host Extra A6/A7 (HXA_SEL)  |
| EX3.13    | Select Host Extra B6/B7 (HXB_SEL)  |
| EX3.14    | Select OTG Extra A6/A7 (OXA_SEL)  |
| EX3.15    | Select OTG Extra B6/B7 (OXB_SEL)  |

How to set the OTG USB 2.0 modes by enabling pins for the two TS5USB41
 
| Mode     | mode bits | A: OE  | A: SEL1/2 | B: OE  | B: SEL1/2 |
|----------|-----------|--------|-----------|--------|-----------|
| off      | 0 0       | H      |           | H      |           |
| Auto USB | 0 1       | L      | 0         | L      | 0         |
| Occi USB | 1 0       | L      | 1         | H      |           |
| Plural   | 1 1       | L      | 0         | L      | 1         |


T-USB OTG 2.0 data,
- off (Autonomous MCU USB talks to Occi MCU USB1)
- Autonomous MCU USB (A and B)
- Occi MCU USB1 (only A)
- Plural; OTG-A connects Autonomous MCU USB, OTG-B connects Extra OTG USB
