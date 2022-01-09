SYS I2C addresses

| Address    | Chipset  | Description               |
|------------|----------|---------------------------|
| 0x20       | PCA9555  | 16 bit expander EX0       |
| 0x21       | PCA9555  | 16 bit expander EX1/USB1  |
| 0x22       | PCA9555  | 16 bit expander EX2/USB2  |
| 0x54..0x57 | EEPROM   |                    |
| 0x47 0x67  | HD3SS220 | USB1 MUX M.2 / T-USB |
| ?          | HD3SS220 | USB2 MUX M.2 / T-USB |
| 0x68 0x6A  | PI6CG18200 | PCIe clock generator |
| 0x70 0x71  | TPS65988 |  PD Controller Port 1 / SYS |
| 0x7E 0x7F  | TPS65988 |  PD Controller Port 2 / i.MX I2C3 |

