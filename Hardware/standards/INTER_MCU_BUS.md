## Inter MCU Bus

A set of pins are connected 1-to-1 between m.2 connectors and MCUs.
The aim is to be able to create efficient connectivity between MCUs based on which ones are currently active.
The bus can connect just two MCUs, but also many. The MCUs must negotiate the use of the bus pins at runtime.

Systems sharing the bus,

- SoM
- T-USB RP2040
- m.2 Key B debug board with MCU
- Debug connector MCU
- T-USB Test board with programmer
- 

Potential protocols,

- SPI / Single or Quad
- I2C (SYS+STEM) ? for coordination
- UART/free pins
- SDIO mode?
- CAN
- USB 2.0

TODO i.MX CAN / SDIO bus allocation.

Implementation refs

- [Raspberry Pi RP2040 gains an extra USB port through PIO’s (programmable I/Os)](https://www.cnx-software.com/2022/02/16/raspberry-pi-rp2040-gains-an-extra-usb-port-through-pio/)

