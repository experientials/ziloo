
The 919 EX6 expander is used for testing m.2 signals on Key B and Key E.
It is on the SYS I2C bus and placed on the Faceboard.
Pins on Key B are prefixed with `B_`.
Pins on Key E are prefixed with `E_`.

The EX6 expander input triggers interrupt via SYS_EX_nINT (GPIO4_IO19).

| Expander  | Connected to    |
|-----------|-----------------|
| EX6.0     | E_COEX4 |
| EX6.1     | E_DEV_WLAN_WAKE      |
| EX6.2     | E_ALERT / I2C_IRQ    |
| EX6.3     | E_LED / DAS / DSS  |
| EX6.4     | E_UART WAKE                |
| EX6.5     | E_SDIO WAKE                |
| EX6.6     | E_LED2#                |
| EX6.8     | B_RESET#      |
| EX6.9     | B_ALERT / I2C_IRQ    |
| EX6.10    | B_LED / DAS / DSS                |
| EX6.11    | B_CONFIG_1                |


