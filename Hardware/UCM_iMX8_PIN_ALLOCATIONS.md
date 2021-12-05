# Pin Allocations

![UCM iMX8M SoM block diagram](./refs/UCM-iMX8M-Plus-System-on-Module-block-diagram.png)


## Unused module pins

Pins not allocated from the 2 * 100 pins connectors of the sb-ucmimx8plus.
The should be configured to something else.

- SPDIF RX / TX
- UART1 RX / TX ?
- UART3 RX / TX ?
- ENET1 RD0 RD1 RD2 RD3 RX_CTL RXC TD0 TD1 TD2 TD3 TX_CTL TXC MDC MDIO nRST INT
- FLEXCAN1_RX (alt SAI2_TXC SAI5_RXD2)  
- FLEXCAN1_TX (alt SAI2_RXC SAI5_RXD1)
- FLEXCAN2_RX (alt SAI2_MCLK SAI5_MCLK)
- FLEXCAN2_TX (alt SAI2_TXD0 SAI5_RXD3)

LVDS pins will not be used, but they don't support muxing.
However I2C3 is used for LVDS, so it is available.


## I2C

- SYS I2C
- CSI I2C5
- CSI I2C6
- DSI LCD I2C2
- I2C3 free (Default used by LVDS)
- I2C4 taken up by PCIe CLKREQ_B

## UART

- UART1 not used
- UART2 is reserved for A53 core debug
- UART3 not used
- UART4 is reserved for M7 core debug


MIPI

- CSI1 uses I2C5 SCL/SDA
- CSI2 uses I2C6 SCL/SDA
- 
- 
- 


## PWM

Any pins free?


## Serial Audio Interface / I2C

Misc connector P20

1  |    | UART2_TXD
3  |    | UART2_RXD
5  |    | PWM1_OUT
7  |    | 3V3_PER
9  |    | -UART1_TXD-  SAI2_RXFS
11 | P1.19   | -UART1_RXD-  SAI2_RXC
13 | P2.62   | SD1_RESET_B
15 | P2.68   | -ENET1_MDC- SAI1_RXD2 (ALT4)
17 | P2.70   | -ENET1_MDIO- SAI1_RXD3 (ALT4)
19 | P2.53   | -ENET1_RX_CTL- SAI1_TXFS (ALT4)
21 | P2.41   | -ENET1_RD0- SAI1_RXD4 (ALT4)
23 | P2.43   | -ENET1_RD1- SAI1_RXD5 (ALT4)
25 | P2.45   | -ENET1_RD2- SAI1_RXD6 (ALT4)
27 | P2.47   | -ENET1_RD3- SAI1_RXD7 (ALT4)
29 | P2.55   | -ENET1_RXC- SAI1_TXC (ALT4)
31 |         | GND
33 |    | I2C3_SCL

2  | P1.61   | -UART3_TXD- 
4  | P1.21   | -UART3_RXD- 
6  |         | 5V0_PER
8  |    | UART4_TXD
10 |    | UART4_RXD
12 | P1.59   | GPIO1_00 
14 | P1.98   | GPIO1_01  
16 | P2.76 ? | -ENET1_nRST-  ? inconsistent  SAI5_TXD1
18 | P2.88 ? | -ENET1_INT-  ? inconsistent  SAI5_TXFS
20 | P2.67   | -ENET1_TX_CTL- SAI1_TXD4 (ALT4)
22 | P2.59   | -ENET1_TD0- SAI1_TXD0 (ALT4)
24 | P2.61   | -ENET1_TD1- SAI1_TXD1 (ALT4)
26 | P2.63   | -ENET1_TD2- SAI1_TXD2 (ALT4)
28 | P2.65   | -ENET1_TD3- SAI1_TXD3 (ALT4)
30 | P2.69   | -ENET1_TXC- SAI1_TXD5 (ALT4)
32 |         | GND
34 |         | I2C3_SDA



Misc connector P21

1 I2C5_SDA
3 I2C5_SCL
5 SYS_I2C_SDA
7 SYS_I2C_SCL
9 GND
11 SAI3_TXD
13 SAI3_TXC
15 SAI3_MCLK
17 SAI3_RXD
19 SAI3_RXC
21 SAI3_TXFS
23 SAI3_RXFS
25 HDMI_HPD
27 ENET TD2_BYPASS
29 HDMI_DDC_SCL
31 HDMI_DDC_SDA
33 HDMI_CEC

2  I2C6_SCL
4  I2C6_SDA
6  GND
8  -CAN2_TX-  SAI5_RDX3
10 -CAN2_RX-  SAI5_MCLK
12 -CAN1_RX-  SAI5_RXD2
14 -CAN1_TX-  SAI5_RXD1
16 SD2_nRST
18 QSPI_BOOT_EN_3P3
20 PCIE_CLKREQ_B
22 ECSPI2_MISO
24 ECSPI2_SS0
26 ECSPI2_SCLK
28 ECSPI2_MOSI
30 USB1_TCPC_nINT
32 USB1_SS_SEL
34 GPIO4_12 / SAI1_TXD0



## SAI5 

Provides 4 lanes out
Provides 4 lanes in
Master clock
Receive clock / frame sync
Transmit clock / frame sync

cannot be used with dev board

- clashes with I2C5 SDA/SCL used for CSI1 & MIPI-DSI touch (SAI5_MCLK, SAi5_RXD0)
- clashes with I2C6 SDA/SCL used for CSI2 (SAI5_RXC, SAI5_RXFS)
- 

## SAI2 

is allocated to CAN1, CAN2, ENET1_nRST, ENET1_INT


## SAI1

Not usable as it clashes with USB1 input interrupt and PCIe WAKE.


General connector 1 provides: TXFS, RXD6, RXD7, TXD4, TXD2, TXD3, TXD5
General connector 2 provides: TXD7, MCLK


- USB1_TCPC_nINT clashes with SAI1_TXD7 (used for GPIO expander int for RESET/FLASH for PCI/UART/DSI/LVDS/CSI1/CSI2)
- USB1_SS_SEL clashes with SAI1_MCLK(used for M.2 PCIE WAKE#)
- Don't use ENET1 !
- Don't use GPIO4_12