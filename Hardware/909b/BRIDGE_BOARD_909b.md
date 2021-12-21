# Bridge Board 909b

The 909b is a Bridge Board version made for testing and experiementation with the Ziloo attachments without attaching
the SB-UCM i.MX8 board or directly attaching it. 
The setup enables connecting a Compulab SB-UCM-iMX8PLUS or [I-Pi SMARC IMX8M Plus](https://www.ipi.wiki/products/i-pi-smarcplus-imx8mp) development board.
Not all the 909 connectors will be mounted on the 801 production bridge board that mounts the i.MX8 board.

The board provides two key features: Dual USB connectivity for Webcam, Internet, Display & Power; MIPI CSI Stereo Camera.
Alt. Mode, HDMI and extra MIPI CSI connectors are not intended for the production board.

- Some of the UCM-iMX8M-Plus carrier board interface pins are multifunctional. Up to 4 functions (ALT modes) are accessible through each multifunctional pin.
- All of the UCM-iMX8M-Plus digital interfaces operate at 3.3V voltage levels unless noted otherwise.
- NOTE: RGMII ENET1 signals operate at 1.8V voltage level
- NOTE: SD/SDIO port #2 can be configured to operate at 3.3V or 1.8V voltage levels. Voltage level is controlled by SoC pin GPIO1_IO04.

![Ziloo Bridge Board 909b](./ziloo-bridge-909b.png)


### Open points

- Add second HD3SS460 for T-USB OTG. 
- Describe T-USB Host ALT connector pinouts with ETH0 pins
- Connect HD3SS460 pins POL AMSEL EN
- Should HD3SS3220 be used to mux between M.2 and T-USB connector?
- Plan I2C addresses and which bus is used
- Can PD Controller control other chipsets or is it just a slave?
- Ensure all pins are connected to GPIO Expander
- Add bridge board EEPROM
- Should there be Boot origin switches like EVK? (4 bits? EVK)
- Add Reset/Power push buttons
- Document Camera sync breakout connector
- Revise the M.2 key type for the second one (currently key E)
- Document connections on the two M.2 connectors


## Connectors

Connectors placed on the board are,

- 2 * [Molex 22PIN 0.5mm pitch 54548-2271](https://www.molex.com/molex/products/part-detail/ffc_fpc_connectors/0545482271)
- 2 * [I-PEX 30PIN 0.4mm pitch 20525-030E-02](https://www.i-pex.com/product/cabline-ca)
- 2 * [Hirose USB-C CX80B1-24P](https://www.hirose.com/product/p/CL0480-0625-0-00)
- 1 * [TE Connectivity 45PIN 0.3MM 571-4-2328724-5 FPC 3-2328724-5](https://www.te.com/usa-en/product-4-2328724-5.html) $0.41
- 2 * [Hirose DF40C-34DS-0.4V](https://www.hirose.com/en/product/p/CL0684-4023-0-51) ([Mouser](https://www.mouser.ch/ProductDetail/Hirose-Connector/DF40C-34DS-04V51?qs=vcbW%252B4%252BSTIpg26DsEbj1iQ%3D%3D))
- 2 * [Hirose DF40HC(3.0)-100DS-0.4V](https://www.hirose.com/en/product/p/CL0684-4151-0-51) mated height 3.0mm
- 1 * microSD card slot (suggested Molex 5031821852) push-push, compact. [Mouser](https://www.mouser.ch/ProductDetail/Molex/503182-1852?qs=s7UCm7gO1bZmpyAhCKZ26g%3D%3D), [Molex](https://www.molex.com/molex/products/part-detail/memory_card_socket/5031821852)
- 1 * MicroHDMI (suggested Molex 46765-1301) [Mouser](https://www.mouser.ch/ProductDetail/Molex/46765-1301?qs=sGAEpiMZZMt1iCLsaqcCFmQhPEZFSo0wUGorAW08d1I%3D) [Molex](https://www.molex.com/molex/products/part-detail/io_connectors/0467651301)
- 1 * [PicoBlade 4 pin 533980471](https://www.molex.com/molex/products/part-detail/pcb_headers/0533980471) for the power ouput. Can be replaced with a higher quality/current connector.
- 1 * m.2 key B connector
- 1 * m.2 key E connector [Amphenol ICC](https://www.amphenol-icc.com/pci-express-10128794004rlf.html)
- 

## Components

- 1 * TPS65982 USB Type-C® and USB PD Controller, Power Switch, and High-Speed Multiplexer
- 1 * HD3SS460 4 x 6 Channels USB Type-CTMAlternate Mode MUX. Connected to T-USB Host
- 2 * push buttons (RESET / POWER)
- 2 * PCA9555 I/O Expander
- 1 * 24C08 Carrier-board EEPROM
- 2 * HD3SS3220  10-Gbps USB 3.1 Type-C 2:1 mux with DRP Controller

![Ziloo Bridge Board 909b back](./ziloo-bridge-909b-back.png)


## USB Power source & Data connectivity

If one(or both) of the USB-C connectors supplies power, it is managed by the USB PD Controller circuit and routed to 
power regulators to provide board power as VIN.

The power connector sends the power from USB-C connectors away from the board as VIN and regulated 5V.
If the USB connectors are not used the power connector can be used to supply the board over VIN.
 
The regulated 5V is also downregulated to 3V3, 2V8 and 1V8 to supply the board with power.

If no connected USB plug connected provides power, the board will have to be a power source. This would be from a yet to be
defined battery connector.

In the specific case of CSI connectors being used without an i.MX8 module attached, the CSI input connectors must
supply power, if no USB connector does.


#### Handling USB Connectors

The two USB ports may power the board. The powering is negotiated and handled by by TPS65988 (in future TPS65994AE).
They also deliver data lanes which are multiplexed between the two USB busses on the i.MX8 module, m.2 connectors and T-USB alt connectors. This allows further development of alt mode connectivity.

Power regulators receive power from USB connectors and supply the VIN & 5V power for development carrier board through the power connector.
The USB-C connectors can power the carrier board 12V through upregulating, which would be done on the In-Between cables.

If one USB port delivers power to the board, the other one can consume power.



## Wiring and Connecting

The board can be used in different ways

1) Adding a daughterboard, two OV2735 camera modules and connecting a USB cable with power.
2) Adding a daughterboard, two RPi camera modules and connecting a USB cable with power.
3) Use the board to connect two OV2735 camera modules to Compulab SB-UCM-iMX8PLUS
4) Use the board to connect two OV2735 camera modules to I-Pi SMARC IMX8M Plus


### Wiring within the board

30 pin CSI connectors are intended to be used without a daughter board and instead a separate i.MX8 development board is used.
The 22 pin connectors are connected directly to the equivalent lines on the 30 pins, and a likewise meant for an external development board or for testing alternate camera modules.
The CSI lanes on 34 pins connector is connected directly to the equivalent lines on the 30 pins.
This assumes that a camera is connected to either a 34 pins connector or a 22 pins connector, not both.
If a i.MX8 daughter board is used rather than development board the CSI lines from the daughter board must
be connected to the 34 pin camera module connectors.
i.MX8 CSI1 is used for left module, CSI2 is used for right module.

The two 34 pin CSI connectors are wired to run in sync via the STROBE pin.


The MicroHDMI connector is connected to the HTMI_TX* pins from the i.MX8 module.

The MicroSD connector is connected to SD2_* on the i.MX8 module.

The USB-C signal lines from the T-USB connector is managed by the Multiplexing chipsets around the PD Controller.

The Power pins on USB-C connectors go to the TPS65988 as well as VIN on 4 pins Power Connector.
GND connected from everywhere as normal.

If power isn't connected over the USB-C plugs, the camera modules should be powered over the MIPI CSI connectors.
In this case it should be possible to use either the 22 pin connectors or the 30 pin connectors for inputting
the signal and power. This means that the 22 pin connectors can be used to input or output MIPI CSI lanes.

For debugging purposes pads must be put on the board for JTAG and debug UARTs 2 & 4.

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

![HDMI connector with eARC](./HDMI-connection.jpg)

![MicroSD connector](./MicroSD.png)


### Multiplexing USB

The i.MX8 has two USB busses. USB1(supports OTG) and USB2(Host mode only).

- USB1 is muxed between the m.2 key E? and the T-USB OTG connector?.
- USB2 is muxed between the m.2 key B and the HD3SS460 for T-USB Host.
- T-USB Host connector is muxed with alternate connections using HD3SS460
- Ethernet may in the future be muxed over T-USB OTG

Open question:

- What should the I2C be used for on TPS65988 Port 1 - 3 ?
- Can PD Controller be wired to control the Alt Mode chips ()


### I/O Expanders

The development board uses a single Expander. The 909 and 801 uses two PCA9555 to control more states
The expanders input triggers interrupt via USB1_TCPC_nINT.

SYS I2C addresses

0x20 PCA9555 16 bit expander
0x21 PCA9555 16 bit expander (2nd) (EX2. / EX3.)
0x54..0x57 EEPROM  I2C slave address: 
? TPS65988 PD Controller


| Expander  | Connected to    |
|-----------|-----------------|
| EX0.0     | mPCIe_PERST on M2    |
| EX0.1     |                 |
| EX0.2     | UART_DEBUGSEL   |
| EX0.3     |                 |
| EX0.4     | _RESET  |
| EX0.5     | _RESET |
| EX0.6     | LVDS_DISP_RESET |
| EX0.7     | LVDS_TOUCH_RESET |
| EX1.0     | CSI1_PWR_DWN_B |
| EX1.1     | LEFT_CAM_RESET  |
| EX1.2     | LEFT_ATT_INT    |
| EX1.3     | LEFT_ATT_XSHUT  |
| EX1.4     | CSI2_PWR_DWN_B  |
| EX1.5     | RIGHT_CAM_RESET |
| EX1.6     | RIGHT_ATT_INT   |
| EX1.7     | RIGHT_ATT_XSHUT |
| EX2.0     | USB_H_ALT_EN    |
| EX2.1     | USB_H_ALT_POL   |
| EX2.2     | USB_H_ALT_AMSEL |
| EX2.3     | USB_O_ALT_EN    |
| EX2.4     | USB_O_ALT_POL   |
| EX2.5     | USB_O_ALT_AMSEL |
| EX2.6     | PD_CTL_INT      |
| EX2.7     | PD_CTL_RESET    |
| EX3.0     |                 |
| EX3.1     |                 |
| EX3.2     |                 |
| EX3.3     |                 |
| EX3.4     |                 |
| EX3.5     |                 |
| EX3.6     |                 |
| EX3.7     |                 |

PD Controller I2C GPIO
- USB_H_ALT_EN, POL, AMSEL
- USB_O_ALT_EN, POL, AMSEL
- 


### I2S (SAI5) 4 channel microphone input mapping

One lane goes to the 34 pins camera connectors

Full connection on the T-USB Alt connectors

| 14  | BCLK / SCK | I2S      | Bit clock line                       | 1.8V |
| 15  | WS / LRCLK | I2S      | Word clock line                      | 1.8V |
| 16  | SDATA1     | I2S      | Input data 1                         | 1.8V |
| 17  | SDATA2     | I2S      | Input data 2 (NC)                    | 1.8V |




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


### Connecting the SB-UCM-iMX8PLUS daughter board

![SB-UCM-iMX8PLUS](../refs/Compulab/ucm-imx8plus_system-on-module_top.jpg)

The daughter board clicks into the two Hirose 100pin board-to-board connectors.

For further details see [Product Page](https://www.compulab.com/products/computer-on-modules/ucm-imx8m-plus-nxp-i-mx-8m-plus-som-system-on-module-computer/).

The CSI1 & CSI2 are wired from the 100pin connectors to relevant CSI connectors.
The CSI1 lanes are connected to Left CSI.
The CSI2 lanes are connected to Right CSI.


- 2 * Hirose 100 pin connectors
- 45 pins connected to Inbetween breakout boards
- 10 pins power connector to Inbetween breakout boards
- USB-C connector to Inbetween breakout boards
- USB-A connector to Inbetween breakout boards


### Connecting the SB-UCM-iMX8PLUS carrier board

![SB-UCM-iMX8PLUS Carrier Board](../refs/SB-UCMIMX8PLUS-carrier-board.jpg)

For further details see [Product Page](https://www.compulab.com/products/carrier-boards/sb-ucmimx8plus-carrier-board/#diagram).

- 2 * I-PEX connector directly between UCM carrier board and bridge board
- 45 pins connected to Inbetween breakout boards
- 10 pins power connector to Inbetween breakout boards
- USB-C connector to Inbetween breakout boards
- USB-A connector to Inbetween breakout boards
- HDMI female to Inbetween breakout boards



## T-USB connector mapping

Two USB-C connectors are arranged in a T shape and the normal way to use it is with a combined connector
attached. This means that the wires will normally be connected in a particular orientation. The system
takes advantage of this by detecting when both USBs are connected in the normal arrangement.

The USB-C signal lines for the OTG connector in T-USB come from USB1(OTG capbale 2.0 & 3.0).
The SBU1/SBU2 are connected to OSBU1/OSBU2 pins on the T-USB alt connector 
One side of the RX/TX pins are carried to  the T-USB alt connector, and not connected to USB1 signals.
(Should the side be muxed?)

The USB-C signal lines for the Host connector in T-USB can be muxed. They either come from USB2(Host only 2.0 & 3.0),
or they come from T-USB alt connector pins prefixed by H*. 
The SBU1/SBU2 on the HD3SS460 are connected to HSBU1/HSBU2.
The Host only USB2 from i.MX8 is Muxed between the T-USB Host connector and the M.2 connector.

The HD3SS460 chips are controlled over I2C by either the MCU using SYS I2C or by the PD Controller.


![USB OTG reference hookup](./USB-OTG-hookup.jpg)


:[T-USB Connector Mapping](../pinouts/T-USB_WITH_ALT_CONNECTOR_PINOUT.md)



#### Power supply TI chipset

TPS65982 USB Type-C® and USB PD Controller, Power Switch, and High-Speed Multiplexer

The TPS65982 device is a stand-alone USB Type-C and Power Delivery (PD) controller providing cable- plug and orientation detection at the USB Type- C connector. Upon cable detection, the TPS65982 device communicates on the CC wire using the USB PD protocol. After successful USB PD negotiation is complete, the TPS65982 enables the appropriate power path and configures alternate mode settings for internal and (optional) external multiplexers.

![Wiring of TPS65988 from datasheet](../datasheets/USB/ref-TPS65988-diagram.png)

A minimal version of this setup should be placed on the 909 to handle power. I.E. No TUSB1044

The 4 pin power connector and T-USB alt connector can be used to test the chipset and USB devices attached.



## Board Power 4 pins Connector

The power connector supplies external boards with power. Max 5V/1A. Max VIN/1A.

:[4 pins Board Power Connector](../pinouts/BOARD_POWER_4_CONNECTOR.md)


## T-USB alt mode connector

This connector(only on the 909 model) enables experimentation with alternate modes and directional pins.

:[45 pins T-USB alt mode connector](../pinouts/T-USB_ALT_CONNECTOR.md)




### RPI FPC 22 pins

Raspberry Pi connectors

- 1-7342485-5  TE Connectivity  15 pins vertical Pi Board A/B
- 54548-2271   Molex 22 pins  Right angle Pi Zero & Compute module
- SFW15R-2STE1LF  Amphenol FCI 15 pins Right angle Camera Module

:[22 pins RPi CSI connector](../pinouts/RPI_22_CONNECTOR.md)


### NVIDIA FPC 30 pins

:[30 pins I-PEX CSI connector](../pinouts/I-PEX_30_CONNECTOR.md)


### Ziloo Camera Module 34 pin connector

**Just to be clear**: All CSI lanes are laid out on one side of the connector with GND between.

:[Camera Module 201 connector](../pinouts/CAMERA_MODULE_CONNECTOR_PINOUT.md)


### Camera Breakout connector 6 pins

| No. | Pin  | Description   |
|-----|------|---------------|
|  1  |	5V   |	Board Power 5V   |
|  2  |	3V3   |	Board Power 3.3V   |
|  3  |	GND  |	   GND 	     |
|  4  | CAM_FSIN   | Frame sync input                     |
|  5  | CAM_STROBE | Frame sync output                    |
|  6  | EXTCLK     | External Clock Input (MCLK)          |

Max. Current per pin 1A