| Signal         | 801 T-USB | BHI260AB     | IS31FL3730 | SOM / MCU | PCA9555 | CAM connectors  | Breakout   |
|----------------|-----------|--------------|------------|-----------|---------|-----------------|------------|
| STEM SDA       | Stem SDA  | Host IF      | STEM SDA   |           |         |                 |            |
| STEM SCL       | Stem SCL  | Host IF      | STEM SCL   |           |         |                 |            |
| SYS SDA        | SYS SDA   |              |            | SYS SDA   | SDA 3V3 |                 |            |
| SYS SCL        | SYS SCL   |              |            | SYS SCL   | SCL 3V3 |                 |            |
| I2C5 SDA       |           | Master 3     |            | I2C5 SDA  |         | Left SCCB       |            |
| I2C5 SCL       |           | Master 3     |            | I2C5 SCL  |         | Left SCCB       |            |
| I2C6 SDA       | NIGHT SDA | Master 2 SDX |            | I2C6 SDA  |         | Right SCCB      |            |
| I2C6 SCL       | NIGHT SCL | Master 2 SCX |            | I2C6 SCL  |         | Right SCCB      |            |
| SPI SCK        |           | M1SCK        |            |           |         |                 | SPI SCK    |
| SPI MOSI       |           | M1SDX        |            |           |         |                 | SPI MOSI   |
| SPI MISO       |           | M1SDI        |            |           |         |                 | SPI MISO   |
|                |           |              |            |           |         |                 |            |
| SYS_EX_nINT    |           |              |            |           | nINT    |                 |            |
|                |           |              | IN         |           |         |                 | LED_AUDIO  |
|                |           |              | C_FILT     |           |         |                 | LED_FILTER |
|                |           | MCSB1        |            |           |         |                 | GPIO       |
|                |           | MCSB2        |            |           |         |                 | GPIO       |
|                |           | MCSB3        |            |           |         |                 | GPIO       |
|                |           | MCSB4        |            |           |         |                 | GPIO       |
|                |           | M1SCX        |            |           |         |                 | M1SCX      |
|                |           | M1SDX        |            |           |         |                 | M1SDX      |
|                |           | M1SDI        |            |           |         |                 | M1SDI      |
|                |           |              |            |           |         |                 |            |
| Signal Level   |           |              | 3.3V       |           | 3.3V    |                 |            |
| Standalone 1V8 |           | Consumes     |            |           |         | VCC_1V8         |            |
| VCC_SOM        | Supplies  |              | Consumes   |           |         |                 | VCC_SOM    |
| Powered 3V3    |           |              |            |           |         | AF_VDD          |            |
| Powered 1V8    |           | Consumes     |            |           |         | DOVDD + VCC_1V8 |            |
| Powered 2V8    |           |              |            |           |         | AVDD_2V8        |            |

