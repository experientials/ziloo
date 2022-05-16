# Bridge Board 909c

The 909c is a Bridge Board version made for testing and experiementation with the Ziloo attachments without attaching
the SB-UCM i.MX8 board or directly attaching it. 
The setup enables connecting a [Compulab SB-UCM-iMX8PLUS](https://www.compulab.com/products/carrier-boards/sb-ucmimx8plus-carrier-board/), [DART-MX8M-PLUS Evaluation Kit](https://www.variscite.com/product/system-on-module-som/cortex-a53-krait/dart-mx8m-plus-nxp-i-mx-8m-plus/#evaluation-kit) or 
[I-Pi SMARC IMX8M Plus](https://www.ipi.wiki/products/i-pi-smarcplus-imx8mp) development board.
Not all the 909 connectors will be mounted on the 801 production bridge board that mounts the i.MX8 board.


Of note in design,

- Some of the UCM-iMX8M-Plus carrier board interface pins are multifunctional. Up to 4 functions (ALT modes) are accessible through each multifunctional pin.
- All of the UCM-iMX8M-Plus digital interfaces operate at 3.3V voltage levels unless noted otherwise.
- RGMII ENET1 signals operate at 1.8V voltage level
- SD/SDIO port #2 can be configured to operate at 3.3V or 1.8V voltage levels. Voltage level is controlled by SoC pin GPIO1_IO04.

![Ziloo Bridge Board 909c](./ziloo-bridge-909c.png)


### Open points

- B2B sound/I2C connectors
- Mux chips shutdown mode
- Should there be Boot origin switches like EVK? (4 bits? EVK)
- Second stage designing a 909 Smiley Board
- Optional connectors debug uart / jtag
- Connection option for Varscite board instead of Compulab
- Annotations and Logo on the board
- TEST The Mux pin configurations


## <mark>Difference from revision B</mark>

- The PD Controller is no longer on the bridge board
- The Power module connects to the bridge board to provide dual USB-C
- Two 20 pin sound connectors
- Only 1 alternative CSI connector for each side
- No Alt USB breakouts on bridge board
- No Alt mode on bridge board
- No I2C breakouts on bridge board
- Only m.2 Key B (no Key E)


## Core Components

- [SB-UCM-iMX8PLUS](https://www.compulab.com/products/computer-on-modules/ucm-imx8m-plus-nxp-i-mx-8m-plus-som-system-on-module-computer/) System-on-Module
- 2 * [Hirose DF40HC(3.0)-100DS-0.4V](https://www.hirose.com/en/product/p/CL0684-4151-0-51) mated height 3.0mm
- 2 * [Hirose DF40-50DS-0.4V](https://www.hirose.com/en/product/p/CL0684-4009-0-51) mated height 1.5mm [Mouser](https://www.mouser.ch/ProductDetail/Hirose-Connector/DF40C-50DS-04V51?qs=sGAEpiMZZMthaSLPVp%252B4asSF8eu6nRoehAaVBEWyQ6A%3D) - [JLCPCB socket](https://jlcpcb.com/parts/componentSearch?isSearch=true&searchTxt=DF40C-50DS-0.4V)
- M.2 key B connector H4.20mm [Amphenol ICC 10128793001RLF](https://www.amphenol-icc.com/pci-express-10128793001rlf.html)
- 2 * [Hirose DF40C-34DS-0.4V](https://www.hirose.com/en/product/p/CL0684-4023-0-51) ([Mouser](https://www.mouser.ch/)
- 1 * microSD card slot (suggested Molex 5031821852) push-push, compact. [Mouser](https://www.mouser.ch/ProductDetail/Molex/503182-1852?qs=s7UCm7gO1bZmpyAhCKZ26g%3D%3D), [Molex](https://www.molex.com/molex/products/part-detail/memory_card_socket/5031821852)
- 1 * [CBTL04083 Multiplexer Switch ICs 3.3V CH 2:1](https://www.nxp.com/part/CBTL04083ABS#/) - [Mouser](https://www.mouser.ch/ProductDetail/NXP-Semiconductors/CBTL04083ABS518?qs=sGAEpiMZZMtRgJo%2FZ%2FMF7P%2Fv50GZnMfoakbaY6SsrwU%3D)
- 2 * PCA9555 I/O Expander
- 1 * [TS5USBC410 Dual 2:1 USB 2.0 Mux/DeMux Switch](../datasheets/USB/ts5usbc41.pdf). [Mouser](https://www.mouser.ch/ProductDetail/Texas-Instruments/TS5USBC410IYFFR?qs=sGAEpiMZZMutXGli8Ay4kPB6XEQFysSpdNErqZgdEYs%3D)


## Dev. Connectors

- 1 * MicroHDMI (suggested Molex 46765-1301) [Mouser](https://www.mouser.ch/ProductDetail/Molex/46765-1301?qs=sGAEpiMZZMt1iCLsaqcCFmQhPEZFSo0wUGorAW08d1I%3D) [Molex](https://www.molex.com/molex/products/part-detail/io_connectors/0467651301)
- 1 * [Molex 22PIN 0.5mm pitch 54548-2271](https://www.molex.com/molex/products/part-detail/ffc_fpc_connectors/0545482271)
- 1 * [I-PEX 30PIN 0.4mm pitch 20525-030E-02](https://www.i-pex.com/product/cabline-ca)
- 1 * [TE Connectivity 45PIN 0.3MM 571-4-2328724-5 FPC 3-2328724-5](https://www.te.com/usa-en/product-4-2328724-5.html) $0.41
ProductDetail/Hirose-Connector/DF40C-34DS-04V51?qs=vcbW%252B4%252BSTIpg26DsEbj1iQ%3D%3D))
- 2 * [Hirose DF40-20DS-0.4V](https://www.hirose.com/product/p/CL0684-4005-9-51) mated height 1.5mm [Mouser](https://www.mouser.ch/ProductDetail/Hirose-Connector/DF40HC35-20DS-04V51) - [JLCPCB socket](https://jlcpcb.com/parts/componentSearch)


## Other Components

Connectors placed on the board are,

- [PI6CG18200 clock](https://www.diodes.com/part/view/PI6CG18200?BackID=2328)
- 1 * 24C08 Carrier-board EEPROM. [Mouser](https://www.mouser.ch/ProductDetail/STMicroelectronics/M24C08-FMN6TP?qs=sGAEpiMZZMtXHE36kCvv38ceEodIXDQNqtU0Mm03QrY%3D)
- 1 * TSM-120-01-F-DV Samtec 2*20 pins surface mounted .100 (Smiley model) [Mouser](https://www.mouser.ch/ProductDetail/Samtec/TSM-120-01-F-DV?qs=rU5fayqh%252BE2gtcIirjF3kA%3D%3D)
- [SuperSpeed MUX PI5USB30213A](https://www.diodes.com/part/view/PI5USB30213A/) may be an option intead of CBTL04083
- [Alternate USB 2.0 Mux/DeMux](https://www.diodes.com/part/view/PI3USB102G/) [Mouser](https://www.mouser.ch/ProductDetail/Diodes-Incorporated/PI3USB102GZLEX?qs=mt7EBqA2jzg7v2qs76v1VQ%3D%3D) [JLCPCB part](https://jlcpcb.com/parts/componentSearch?isSearch=true&searchTxt=DF40C-60DS-0.4V)
- 5 * TXB0108 voltage shifters 3.3V to 1.8V

![Ziloo Bridge Board 909c back](./ziloo-bridge-909c-back.png)

The back of the board connects for SB-UCM-iMX8PLUS, T-USB module and M.2 Key B module.
The SB-UCM-iMX8PLUS is the center of the board and receives all signals.


# Power supply, CSI, I2S & I2C

The USB-C connectors can supply power, as can the 30 pins and 22 pins CSI connectors.
The 34 pins connector outputs CSI, I2S, I2C, Power and control pins.
Voltages needed are 3V3, 2V8, 1V8. 2V8 is only needed for the camera module.

In the specific case of CSI connectors being used without an i.MX8 module attached, the CSI input connectors must
supply power, if no USB connector does.

According to the UCM-IMX8PLUS Referene Guide the Supply Voltage is 3.45V to 4.4V.
VSOM from the Power module provides this level. 


## System Power

:[Power Module Connection](../refs/POWER_MODULE_CONNECT.md)
 
The module connectors have pins that are used for different setups. Not all should be connected to the 909 board.

VIN_3V3 and VIN_5V can be supplied externally via a soldering pad for experimental purposes.


## Camera CSI Connectors

### CSI connectors

The CSI connectors data lanes are connected directly together for each side. It is only possible 
to connect a single left and a single right camera module at a time.

The 22 pin and 30 pin CSI connectors are intended to be used without a daughter board and instead a separate i.MX8 development board is used.
The CSI lanes on 34 pins connector is connected directly to the equivalent lines on the 30 pins.
This assumes that a camera is connected to either a 34 pins connector or a 22 pins connector, not both.
If a i.MX8 daughter board is used rather than development board the CSI lines from the daughter board must
be connected to the 34 pin camera module connectors.
i.MX8 CSI1 is used for left module, CSI2 is used for right module.

The two 34 pin CSI connectors are wired to run in sync via the STROBE pin.

If power isn't connected over the USB-C plugs, the camera modules should be powered over the MIPI CSI connectors.
In this case it should be possible to use either the 22 pin connectors or the 30 pin connectors for inputting
the signal and power. This means that the 22 pin connectors can be used to input or output MIPI CSI lanes.

SCCB for CSI1 is connected to I2C5 voltage shifted.
SCCB for CSI2 is connected to I2C6 voltage shifted.


#### Microphone I2S mapping (SAI5)

The microphone I2S mapping is done by using AL2 mode for the SAI3 pads to get SAI5 signals.
[Multiplexed Signal Pins](./ucm-imx8plus_multifunctional.pdf).
The microphones on the 6 pins and 34 pins connector use SAI5_RX_DATA0.

| Misc pin | SoM pin | i.MX pad      | Functionality     | ALT       | On 6 pin connector |
|----------|---------|---------------|-------------------|-----------|--------------------|
| 11       | P1.26   |  SAI3_TXD     |  SAI5_RX_DATA3    | ALT2      |      |
| 17       | P1.28   |  SAI3_RXD     |  SAI5_RX_DATA0    | ALT2      | DATA    |
| 15       | P1.30   |  SAI3_MCLK    |  SAI5_MCLK        | ALT2      |      |
| 19       | P1.32   |  SAI3_RXC     |  SAI5_RXC         | ALT2      | BCLK    |
| 23       | P1.34   |  SAI3_RXFS    |  SAI5_RX_SYNC     | ALT2      | LRCLK    |
| 13       | P1.36   |  SAI3_TXC     |  SAI5_RX_DATA2    | ALT2      |      |
| 21       | P1.38   |  SAI3_TXFS    |  SAI5_RX_DATA1    | ALT2      |      |


#### Speaker I2S mapping (SAI5)

ENET1 are mapped as SAI5 and brought out as speaker 6 pins connector.
[Multiplexed Signal Pins](./ucm-imx8plus_multifunctional.pdf).

| Misc pin | SoM pin | i.MX pad              | Functionality     | On 6 pin connector |
|----------|---------|-----------------|-------------------|-----------|--------------------|
| 15       | P1.30   |  SAI3_MCLK      |  SAI5_MCLK        | ALT2      |      | 
|          | P2.53   | ENET1_RX_CTL    | SAI5_TXFS         | ALT       | LRCLK     |
|          | P2.55   | ENET1_RXC       | SAI5_TXC / BCLK   | ALT       | BCLK     |
|          | P2.60   | ENET1_TD0       | SAI5_TXD0         | ALT       | DATA     |
|          | P2.63   | ENET1_TD2       | SAI5_TXD2         | ALT       |      |
|          | P2.65   | ENET1_TD3       | SAI5_TXD3         | ALT       |      |
|          | P2.76   | ENET1_nRST IO24 | SAI5_TXD1         | ALT       |      |


##### CAN1 / CAN2 mapping Soldering Pads

CAN1 and CAN2 brought out as soldering pads.
[Multiplexed Signal Pins](./ucm-imx8plus_multifunctional.pdf).

| Misc pin | SoM pin | i.MX pad              | Functionality     | ALT       |
|----------|---------|-----------------------|-------------------|-----------|-------
| 8        | P1.33   | CAN2_TX  |           |      | 
| 10       | P1.49   | CAN2_RX  |           |      | 
| 12       | P1.51   | CAN1_RX   |            |      | 
| 14       | P1.53   | CAN1_TX   |            |      | 



### Connecting the SB-UCM-iMX8PLUS SoM

The daughter board clicks into the two Hirose 100pin board-to-board connectors.

For further details see [Product Page](https://www.compulab.com/products/computer-on-modules/ucm-imx8m-plus-nxp-i-mx-8m-plus-som-system-on-module-computer/).

The CSI1 & CSI2 are wired from the 100pin connectors to relevant CSI connectors.
The CSI1 lanes are connected to Left CSI.
The CSI2 lanes are connected to Right CSI.
The USB1 and USB2 data will be connected to multiplexers
The 45 pins Debug connector will break out many additional signal lines

- 2 * Hirose 100 pin connectors are used to connect the SoM daughter board


![SB-UCM-iMX8PLUS](../refs/Compulab/ucm-imx8plus_system-on-module_top.jpg)


# MicroSD, MicroHDMI, M.2 key B & Debug Breakout

The MicroHDMI connector is connected to the HTMI_TX*, HDMI_DDC_*, HDMI_CEC, HDMI_HPD pins from the i.MX8 module.

The MicroSD connector is connected to SD2_DATA*, SD2_CLK, SD2_CMD, SD2_nCD on the i.MX8 module.

![HDMI connector with eARC](./HDMI-connection.jpg)

![MicroSD connector](./MicroSD.png)


### M.2 Key B

See EXPANSION document for more information.

Note that some pins are connected to I/O Expander 2 meant for USB2 and Key B.
Also, there will be no fastening screw for the m.2 board.


### Debugging Breakout connector

See end of this document for pinouts.


# T-USB Module Data Connection

:[T-USB Mounting instructions](../801-T-USB/T-USB-MOUNT.md)


### I2C EEPROM

Add an EEPROM like 24C08 present on the UCM carrier board.


## Wiring and Connecting

The board can be used in different ways

1) Adding a daughterboard, two OV2735 camera modules and connecting a USB cable with power.
2) Adding a daughterboard, two RPi camera modules and connecting a USB cable with power.
3) Use the board to connect two OV2735 camera modules to Compulab SB-UCM-iMX8PLUS
4) Use the board to connect two OV2735 camera modules to I-Pi SMARC IMX8M Plus



Signal voltage level 

- 201 Camera Module uses 1.8V signals
- IMX477 sensor uses 1.8V for signals
- Does RPi cam module level shift the signals?
- UMC iMX8PLUS module uses 3.3V for signals by default
- UMC iMX8PLUS module RGMII ENET1 signals operate at 1.8V voltage level
- iMX8M plus is documented to use VDD_MIPI_1P8 power group for CSI1 & CSI2
- iMX8M plis is documented to use VDD_HDMI_1P8 power group for HDMI
- NVCC_SAI1_SAI5 power group?
- What will the I2C 5+6 power group be?
- USB 1 & 2 uses VDD_USB_3P3 power group
- Signal voltage PD Controller?


Required distances/location

- Camera module distance 70mm
- USB-C connectors cannot be moved
- Board size can only be increased to save cost
- Holes in the corners should be the regular sort for mounting.
- 

### I/O Expanders

Two expanders are placed on the bridge board and a third is on the Power Module.

:[SYS I2C GPIO Expander 0](../pinouts/I2C_EXPANDER_0.md)
I/O Expander like Compulab Carrier Board to map Camera interrupts.

:[SYS I2C GPIO Expander 2](../pinouts/I2C_EXPANDER_2.md)
I/O Expander to cover m.2 Expander

:[SYS I2C addresses](../pinouts/SYS_I2C_ADDRESSES.md)


### I2S (SAI5) 4 channel microphone input mapping

One lane goes to the 34 pins camera connectors

The full 4 lanes are available on the debug connector and M.2 Key B.



### <mark>Signal Interrupt(INT) pins</mark>

Various chips have internal state changes that should cause interrupts by the SoM(CPU).
It is essential that inputs are flagged so communication can be reliable.

On the reference board these are triggered via USB1_TCPC_nINT(P1.60)
It is used for USB-C orientation changes and I/O Expander 0 inputs.

Events that we want to catch

- T-USB OTG plug events
- T-USB Host plug events
- PD Controller state changed
- Camera sensors input ready
- I/O Expander input ready
- m.2 connectors
- PCIe

Interrupts from the PD Controller are input to I/O Expander 0 (or 3). It in turn
triggers an interrupt on EX0_nINT or EX_T_nINT.

Interrupts from the Left and right cameras interrupt signal(ATT_INT) is connected
to I/O Expander 0.
It in turn triggers an interrupt on EX0_nINT.

Direct/Indirect interrupt triggers

| Chip           | Chip pin     | SoM pin       | Description               |
|----------------|--------------|---------------|---------------------------|
| PDA9555 EX 0   | INT          | EX0_nINT      | Original Expander - P1.60        |
| PDA9555 EX 2   | INT          | EX_OH_nINT    | USB2 Host and M.2 Key B - P1.59  |
| PDA9555 EX 3   | INT          | EX_T_nINT     | Separate T-USB module Expander - P1.98 |
| PCIe m.2 Key B | WAKE#        | PCIE_WAKE_B   | m.2 Key B - P2.52                |
| PCIe m.2 Key B | CLKREQ#      | PCIE_CLKREQ_B | m.2 Key B - P2.90                |
| Left Sensors   | ATT_INT      | -             | Left Camera Module sensors |    
| Right Sensors  | ATT_INT      | -             | Right Camera Module sensors |
| PD I2C 1       | PD_CTL_INT_1 | -             | PD Controller   |   
| PD I2C 2       | PD_CTL_INT_2 | -             | PD Controller   |   



### 8.1 Carrier Board Design Guidelines

APPLICATION NOTES from  UCM-iMX8M-Plus Reference guide.

- Ensure that all V_SOM and GND power pins are connected.
- Major power rails - V_SOM and GND must be implemented by planes, rather than traces. Using at least two planes is essential to ensure the system signal quality because the planes provide a current return path for all interface signals.
- It is recommended to put several 10/100uF capacitors between V_SOM and GND near the mating connectors.
- Except for a power connection, no other connection is mandatory for UCM-iMX8M-Plus operation. All power-up circuitry and all required pullups/pulldowns are available onboard UCM-iMX8M-Plus.
- If for some reason you decide to place an external pullup or pulldown resistor on a certain signal (for example - on the GPIOs), first check the documentation of that signal provided in this manual. Certain signals have on-board pullup/pulldown resistors required for proper initialization. Overriding their values by external components will disable board operation. For details please refer to section Error! Reference source not found..
- You must be familiar with signal interconnection design rules. There are many sensitive groups of signals. For example:
- PCIe, Ethernet, USB and more signals must be routed in differential pairs and by a controlled impedance trace.
- Audio input must be decoupled from possible sources of carrier board noise.
- The following interfaces should meet the differential impedance requirements with
manufacturer tolerance of 10%:
- USB2.0: DP/DM signals require 90 ohm differential impedance.
- All single-ended signals require 50 ohm impedance.
- PCIe TX/RX data pairs and PCIe clocks require 85 ohm differential impedance.
- Ethernet, MIPI-CSI and MIPI-DSI signals require 100 ohm differential impedance.
- The carrier board interface connectors provide 3mm mating height. Bear in mind that there are components on the bottom side of UCM-iMX8M-Plus. It is not recommended to place any components underneath the UCM-iMX8M-Plus module.
- Refer to the SB-UCMIMX8PLUS carrier board reference design schematics.
- It is recommended to send the schematics of the custom carrier board to Compulab
support team for review.

V_SOM is recommended between 3.45 and 4.4 volt, typical 3.7

for more information see [UCM i.MX8 PLUS Reference Guide](../datasheets/i.MX8/ucm-imx8plus_reference-guide_2021-11-02.pdf)


### Connecting the SB-UCM-iMX8PLUS carrier board

![SB-UCM-iMX8PLUS Carrier Board](../refs/SB-UCMIMX8PLUS-carrier-board.jpg)

For further details see [Product Page](https://www.compulab.com/products/carrier-boards/sb-ucmimx8plus-carrier-board/#diagram).

- 2 * I-PEX connector directly between UCM carrier board and bridge board
- 45 pins connected to Inbetween breakout boards
- 10 pins power connector to Inbetween breakout boards
- USB-C connector to Inbetween breakout boards
- USB-A connector to Inbetween breakout boards
- HDMI female to Inbetween breakout boards



# 909c Connector Pinouts

## Debugging Breakout connector

:[Debugging Breakout connector](../pinouts/DEBUG_BREAKOUT_CONNECTOR_PINOUT.md)


## 50 pin B2B connectors

:[DF40 50 pin connectors](../pinouts/T-USB_50_PINS_CONNECTORS.md)


## RPI FPC 22 pins

On the left(CSI1) side.

:[22 pins RPi CSI connector](../pinouts/RPI_22_CONNECTOR.md)


## NVIDIA FPC 30 pins

On the right(CSI2) side.

:[30 pins I-PEX CSI connector](../pinouts/I-PEX_30_CONNECTOR.md)


## Ziloo Camera Module 34 pin connector

**Just to be clear**: All CSI lanes are laid out on one side of the connector with GND between.

:[Camera Module 201 connector](../pinouts/CAMERA_MODULE_CONNECTOR_PINOUT.md)


## Sound connector 20 pins

There are two connectors that provide the same signals.

:[Sound Connector](../pinouts/SOUND_CONNECTOR.md)


## <mark>Soldering Pads</mark>

A number of connections should be broken out on the board as soldering pads (no through hole)

| Pin       | Function                |
|-----------|-------------------------|
| VSOM      | Output or Input         |
| VCC_RTC   | Power input RTC battery |
| VIN_5V    | T-USB System 5V  |
| VIN_3V3   | T-USB System 3.3V |
| PD_VIN_EN | T-USB pin PD_VIN_EN Breakout |
| GND       |                         |
| P1.33     | CAN2_TX                 |           
| P1.49     | CAN2_RX                 |           
| P1.51     | CAN1_RX                 |          
| P1.53     | CAN1_TX                 |          
| SAI5_TXC  | I2S Speaker Bit clock line  (BCLK/SCK)  P2.55  |
| SAI5_TXFS | I2S Speaker Word clock line (WS/LRCLK)  P2.53  |
| SAI5_TXD0 | I2S Speaker data 1  P2.60            |
| SAI5_TXD1 | I2S Speaker data 2  P2.76      |
| SAI5_TXD2 | I2S Speaker data 3  P2.63      |
| SAI5_TXD3 | I2S Speaker data 4  P2.65      |


## M.2 B and Other Expansion Slots 

See `EXPANSION.pdf` / `EXPANSION.md`


