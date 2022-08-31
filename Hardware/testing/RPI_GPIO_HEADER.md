| Left side                  | Function  |Pin |Pin | Function  | Right side           |
|----------------------------|-----------|----|----|-----------|----------------------|
|  When VSOM fully connected | 3V3       | 1  | 2  | 5V        | When VSOM fully connected  |
|                  STEM_SDA  | SDA       | 3  | 4  | 5V        | When VSOM fully connected |
|                  STEM_SCL  | SCL       | 5  | 6  | GND       |                      |
|                   STEM_INT | INT       | 7  | 8  | TxD       | UART2 TxD            |
|                            | GND       | 9  | 10 | RxD       | UART2 RxD            |
|                            |           | 11 | 12 | SWD       | SWDCLK for T-USB     |
|     SDIO DAT3 / GPIO2_IO18 | SDIO      | 13 | 14 | SWD       | SWDIO for T-USB (GND)     |
|      SDIO CLK / GPIO2_IO13 | SDIO      | 15 | 16 | SDIO      | SDIO CMD / GPIO2_IO14  |
|                            | 3V3       | 17 | 18 | SDIO      | SDIO DAT0 / GPIO2_IO15 |
| ECSPI2_MOSI / GPIO5_IO11   | MOSI      | 19 | 20 | GND       |                        |
| ECSPI2_MISO / GPIO5_IO12   | MISO      | 21 | 22 | SDIO      | SDIO DAT1 / GPIO2_IO16 |
| ECSPI2_SCLK / GPIO5_IO10   | SCLK      | 23 | 24 | SPI CE0   | ECSPI2_SS0/GPIO5_IO13  |
|                            | GND       | 25 | 26 | SCL       | NIGHT SCL            |
|                    SYS I2C | SYS SDA   | 27 | 28 | SCL       | SYS I2C              |
|                  NIGHT_INT | INT       | 29 | 30 | (GND)     |                      |
|                  NIGHT_SDA | SDA       | 31 | 32 | TxD       | UART4 TX             |
|                   UART4 RX | RxD       | 33 | 34 | JTAG      | GND                   |
|                            |           | 35 | 36 | JTAG      |                       |
|     SDIO DAT2 / GPIO2_IO17 | SDIO      | 37 | 38 | CAN2      |                       |
|               (GND on RPi) |           | 39 | 40 | CAN2      |                       |


SWDIO
MIC DAT
MIC CLK
HUMAN DAT
RP UART RX/TX

RP Power on
RP Bootsel

MSP_SBWTDIO
MSP_SBWTCK