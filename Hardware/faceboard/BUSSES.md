## Busses going through the Faceboard

- UART1 connected to UART_T_*XD on 50 pin T-USB connector and to SoM
- UART2 connects M.2 Key B BT/LPWAN UART and to SoM, is also used for A53 core debug
- UART3 connected to UART_F_*XD on Faceboard Extender and to SoM.
- UART4 is reserved for M7 core debug
- Stem I2C is primarily used to communicate between MCUs that can pass master role between them
- Day I2C is Sensor I2C on the Left Camera?
- Night I2C is Sensor I2C on the Right Camera?
- SYS I2C is mastered by the SoM while awake to control PCIe, RT Clock, and PMIC.

- Host USB 2.0 defaults to M.2 connector, but can be switched to 50 pin connector
- Should OTG USB 2.0 optionally be routed to Key E ?
- PCIe single lane to M.2 Key B
- 