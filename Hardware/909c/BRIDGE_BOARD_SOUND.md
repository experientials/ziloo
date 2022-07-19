
# Sound Connector

<mark>This connector is new, it replaces the 6 pin</mark>

The sound connector provides 4 lines input and 4 lines output. They connect
directly to the System Module, so they are not level shifted.
It is not yet defined if the signal level is 1.8V or 3.3V. It will depend on NVCC_SAI5
The pin layout wraps around aligning 1 and 20 close, but on opposite sides.

Two Connector components used are [DF40HC(3.5)-20DS-0.4V(51)](https://www.hirose.com/en/product/p/CL0684-4188-0-51). [Socket @ Mouser](https://www.mouser.ch/ProductDetail/Hirose-Connector/DF40HC35-20DS-04V51?qs=sGAEpiMZZMtJbfcMcIM8CC3aG3XFbLOWRtCXQ0n%252BY5Y%3D)

:[Sound Connector](../pinouts/SOUND_CONNECTOR.md)



### I2S (SAI5) 4 channel microphone input mapping

One lane goes to the 34 pins camera connectors
The microphones on the 34 pins connector use SAI5_RX_DATA0.

The full 4 lanes are available on the sound connector and M.2 Key B.


#### Microphone I2S mapping (SAI5)

The microphone I2S mapping is done by using AL2 mode for the SAI3 pads to get SAI5 signals.
[Multiplexed Signal Pins](./ucm-imx8plus_multifunctional.pdf). 
This provides the 4 microphone lines on the Sound Connector.

| Misc pin | SoM pin | i.MX pad      | Functionality     | ALT       | I2S                |
|----------|---------|---------------|-------------------|-----------|--------------------|
| 11       | P1.26   |  SAI3_TXD     |  SAI5_RX_DATA3    | ALT2      |      |
| 17       | P1.28   |  SAI3_RXD     |  SAI5_RX_DATA0    | ALT2      | DATA0    |
| 15       | P1.30   |  SAI3_MCLK    |  SAI5_MCLK        | ALT2      |      |
| 19       | P1.32   |  SAI3_RXC     |  SAI5_RXC         | ALT2      | BCLK    |
| 23       | P1.34   |  SAI3_RXFS    |  SAI5_RX_SYNC     | ALT2      | LRCLK    |
| 13       | P1.36   |  SAI3_TXC     |  SAI5_RX_DATA2    | ALT2      |      |
| 21       | P1.38   |  SAI3_TXFS    |  SAI5_RX_DATA1    | ALT2      |      |


#### Speaker I2S mapping (SAI5)

ENET1 are mapped as SAI5 and brought out as speaker on 20 pins Sound connector.
[Multiplexed Signal Pins](./ucm-imx8plus_multifunctional.pdf).

| Misc pin | SoM pin | i.MX pad              | Functionality           | I2S |
|----------|---------|-----------------|-------------------|-----------|--------------------|
| 15       | P1.30   |  SAI3_MCLK      |  SAI5_MCLK        | ALT2      |      | 
|          | P2.53   | ENET1_RX_CTL    | SAI5_TXFS         | ALT       | LRCLK     |
|          | P2.55   | ENET1_RXC       | SAI5_TXC / BCLK   | ALT       | BCLK     |
|          | P2.60   | ENET1_TD0       | SAI5_TXD0         | ALT       | DATA 0    |
|          | P2.63   | ENET1_TD2       | SAI5_TXD2         | ALT       |      |
|          | P2.65   | ENET1_TD3       | SAI5_TXD3         | ALT       |      |
|          | P2.76   | ENET1_nRST IO24 | SAI5_TXD1         | ALT       |      |


## Sound connector 20 pins

<mark>This connector is new</mark>

There are two connectors that provide the same signals.

:[Sound Connector](../pinouts/SOUND_CONNECTOR.md)
     

