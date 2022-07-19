
This 919 EX4 Faceboard sensor I/O Expander is placed on faceboard and controlled via the Stem I2C.

- LED Controller
- Motion Sensor
- Sound Sensor
- Nighttime camera attached sensors
- 

The EX4 expander input triggers interrupt via STEM_INT.

| Expander  | Connected to                |
|-----------|-----------------------------|
| EX4.2     | SD Card Chip Select         |
| EX4.3     | IMU_INTM - MC6470 INTM      |
| EX4.4     | IMU_IRQ - MC6470 INTA / Motion Controller  |
| EX4.5     | IMU_RESETN  - Motion Controller    |
| EX4.6     | IMU_MODE  - Motion Controller        |
| EX4.7     | LED_SHUTDOWN - SDB         |
| EX4.8     | MIC VM3011 DOUT            |
| EX4.9     | W_DISABLE2# on m.2 Key E   |
| EX4.10    | W_DISABLE1# on m.2 Key E   |
| EX4.11    | M2E_PWROFF on m.2 Key E    |
| EX4.12    | M2B_PWROFF on m.2 Key B    |
| EX4.13    | DEVSLP 3V3 on m.2 Key B    |
| EX4.14    | RIGHT_ATT_INT              |
| EX4.15    | RIGHT_ATT_XSHUT            |

Enable CS SD Card connector
LCD CS SPI
MMC CS 
m.2 WiFi CS SDIO
