### DF9 31 pin connector (without emboss)

DF9-31S-1V(32) DF9-31P-1V(22) tin plated, socket/plug

500 mA per pin
Mated height 4.3mm/4.5mm height

6 VSOM and GND pins for 3A.


| Pin | Code         | Type     | Details                              | Voltage |
|-----|--------------|----------|--------------------------------------|---------|
| 1   | VSOM         | Power    | Main power for board 3.45V - 4.5V    |         |
| 2   | GND          | Power    | Ground                               |         |
| 3   | USB1_DP      | USB      | USB1 D+                              |         |
| 4   | USB1_DN      | USB      | USB1 D-                              |         |
| 5   | GND          | Power    | Ground                               |         |
| 6   | USB2_DP      | USB      | USB2 D+                              |         |
| 7   | USB2_DN      | USB      | USB2 D-                              |         |
| 8  | GND          | Power    | Ground                               |         |
| 9  | VSOM         | Power    | Main power for board 3.45V - 4.5V    |         |
| 10  | SYS_nINT     | IRQ      | Interrupt signal (GPIO4_IO19)        |      |
| 11  | EX_OH_nINT   | IRQ      | Interrupt signal (GPIO1_IO0)         |      |
| 12  | EX_T_nINT    | IRQ      | Interrupt signal (GPIO1_IO1).        |      |
| 13  | VSOM         | Power    | Main power for board 3.45V - 4.5V    |         |
| 14  | GND          | Power    | Ground                               |         |
| 15  | SYS_RST_PMIC | Reset    | PMIC reset input pin. Internally pulled up with LDO1 power rail. Once low, PMIC performs reset. |         |
| 16  | POR_B_3P3    | Reset    | Power On reset output pin. Open drain output requiring external pull up resistor. |    |
| 17  | PMIC_ON_REQ  | Reset    | PMIC ON input from Application processor. When high, the device starts power on sequence. |     |
| 18  | PMIC_STBY_REQ| Reset    | Standby mode input from Application processor. When high, device enters STANDBY mode. |     |
| 19  | VSOM         | Power    | Main power for board 3.45V - 4.5V    |         |
| 20  | VCC_RTC      | Power    | Low power mode supply                |         |
| 21  | GND          | Power    | Ground                               |         |
| 22  | PWRBTN       | Boot     | Power button trigger                 |         |
| 23  | ALT_BOOT     | Boot     | Alternate boot                       |         |
| 24  | QSPI_BOOT_EN_3P3| Boot  | SPI boot                             |         |
| 25  |              | Reserved |                                      |         |
| 26  |              | Reserved |                                      |         |
| 27  |              | Reserved |                                      |         |
| 28  |              | Reserved |                                      |         |
| 29  |              | Reserved |                                      |         |
| 30  | GND          | Power    | Ground                               |         |
| 31  | VSOM         | Power    | Main power for board 3.45V - 4.5V    |         |

