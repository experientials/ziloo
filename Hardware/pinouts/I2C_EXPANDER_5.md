
The 919 EX5 expander is used for testing m.2 signals on Key B and Key E.
It is on the SYS I2C bus.

The EX5 expander input triggers interrupt via EX0_nINT (GPIO4_IO19).

| Expander  | Connected to    |
|-----------|-----------------|
| EX5.0     | E_COEX4 |
| EX5.1     | E_DEV_WLAN_WAKE      |
| EX5.2     | E_ALERT / I2C_IRQ    |
| EX5.3     | E_LED / DAS / DSS  |
| EX5.4     | E_UART WAKE                |
| EX5.5     | E_SDIO WAKE                |
| EX5.6     | E_LED2#                |
| EX5.8     | B_RESET#      |
| EX5.9     | B_ALERT / I2C_IRQ    |
| EX5.10    | B_LED / DAS / DSS                |
| EX5.11    | B_CONFIG_1                |


