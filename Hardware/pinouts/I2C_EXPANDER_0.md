The development board uses a single Expander. The 909 and 801 uses 4x PCA9555 to control more states
The system expander input triggers interrupt via EX0_nINT (GPIO4_IO19).

This first expander, which is also on the dev. board maps,

| Expander  | Connected to    |
|-----------|-----------------|
| EX0.0     | mPCIe_PERST on M2 Key B    |
| EX0.1     | mPCIe_PERST on M2 Key E   |
| EX0.2     |                 |
| EX0.3     | PD_CTL_INT_1    |
| EX0.4     | PD_CTL_INT_2     |
| EX0.5     | PD_CTL_RESET     |
| EX0.6     |  |
| EX0.7     |  |
| EX0.8     | CSI1_PWR_DWN_B |
| EX0.9     | LEFT_CAM_RESET  |
| EX0.10    | LEFT_ATT_INT    |
| EX0.11    | LEFT_ATT_XSHUT  |
| EX0.12    | CSI2_PWR_DWN_B  |
| EX0.13    | RIGHT_CAM_RESET |
| EX0.14    | RIGHT_ATT_INT   |
| EX0.15    | RIGHT_ATT_XSHUT |

