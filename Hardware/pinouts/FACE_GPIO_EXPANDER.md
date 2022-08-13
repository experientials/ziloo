| Function          | VQFN32 | LQFP | G56 | Connected to             |
|-------------------|--------|------|-----|--------------------------|
| IMU_INTM          | 9      | 40   | 42  | P2.0. IMU Motion Interrupt   |
| IMU_INTA          | 10     | 39   | 41  | P2.1. IMU Accelerator Interrupt   | 
| POR_B_3P3         | 11     | 38   | 40  | P2.2. Power on reset Input from PMIC. 50 pin connector             | ?
| (BOTH_VSOM)       | 15     | 37   | 39  | P2.3. Input from faceboard. 50 pin connector    | 
| SD2_CS            | 16     | 36   | 38  | P2.4. Input/Output of SD Card Chip Select      |
|                   | 17     | 35   | 37  | P2.5.    |
| LEFT_ATT_INT      | 26     | 34   | 36  | P2.6. Left CAM        |
| RIGHT_ATT_INT     | 25     | 33   | 35  | P2.7. Right CAM |
| LED_SHUTDOWN - SDB| SH1.0  | 56   | 56  | P3.0.   |
|                   | SH1.1  | 55   | 55  | P3.1.   |
| CSI1_PWR_DWN_B    | SH1.2  | 54   | 54  | P3.2. Left CAM        |
| LEFT_CAM_RESET    | SH1.3  | 53   | 53  | P3.3. Left CAM        |
| LEFT_ATT_XSHUT    | SH1.4  | 52   | 52  | P3.4. Left CAM        |
| CSI2_PWR_DWN_B    | SH1.5  | 51   | 51  | P3.5. Right CAM |
| RIGHT_CAM_RESET   | SH1.6  | 50   | 50  | P3.6. Right CAM |
| RIGHT_ATT_XSHUT   | SH1.7  | 49   | 49  | P3.7. Right CAM |
| PWRBTN            | SH2.0  | 5     | 11  | P4.3. 50 pin connector    |
| ALT_BOOT          | SH2.1  | 4     | 10  | P4.4. 50 pin connector    |
|                   | SH2.2  | 3     | 9   | P4.5. 50 pin connector    |
|                   | SH2.3  | 2     | 8   | P4.6.   |
| SYS_RST_PMIC      | SH2.4  | 1     | 7   | P4.7. 50 pin connector   |
| PMIC_ON_REQ       | SH2.5  | 28    | 30  | P5.4. 50 pin connector  |
| PMIC_STBY_REQ     | SH2.6  | 27    | 29  | P5.5. 50 pin connector  |
|                   | SH2.7  |       |     |                 |        
| B_CONFIG_1        |        | 48    | 48  | P6.0. m.2 Key B |
| B_CONFIG_2        |        | 47    | 47  | P6.1. m.2 Key B  |
| B_CONFIG_3        |        | 46    | 46  | P6.2. m.2 Key B  |
|                   |        | 45    | 45  | P6.3. m.2 Key B  |
| M2B_PWROFF        | SH3.0  | 44    | 44  | P6.4. m.2 Key B   |
| M2B_RESET         | SH3.1  | 43    | 43  | P6.5. m.2 Key B   |
| GNSS_IRQ          | SH3.2  | 6     | 6   | P7.0. on m.2 Key B   |
| M2E_PWROFF        | SH3.3  | 5     | 5   | P7.1. on m.2 Key E   |
| W_DISABLE1#       | SH3.4  | 4     | 4   | P7.2. on m.2 Key E   |
| W_DISABLE2#       | SH3.5  | 3     | 3   | P7.3.     | 
|                   | SH3.6  | 60    | 2   | P7.4.    |
|                   | SH3.7  | 59    | 1   | P7.5.     |

56 pin package excludes 8 pins: P8.0 P8.1 P5.6 P5.7 P6.6 P6.7 P7.6 P7.7 (only usable at 64 pin package)

TODO receive SD2_CS
TODO GPIO11 (WAKE_ON_WWAN) ?

TODO USB2 Host mux select 50 pin and M.2 Key B. USB2 OTG mux select 50 pin and M.2 Key E?

TODO remove boot controls?

TODO Consider integration of Key E pins,

| Expander  | Connected to    |
|-----------|-----------------|
| EX6.0     | E_COEX4 |
| EX6.1     | E_DEV_WLAN_WAKE      |
| EX6.2     | E_ALERT / I2C_IRQ    |
| EX6.3     | E_LED / DAS / DSS  |
| EX6.4     | E_UART WAKE                |
| EX6.5     | E_SDIO WAKE                |
| EX6.6     | E_LED2#                |
| EX6.10    |                 |
