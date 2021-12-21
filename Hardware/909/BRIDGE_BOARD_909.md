# Bridge Board 909

The 909 is a Bridge Board version made for testing and experiementation with the Ziloo attachments without attaching
the i.MX8 board. The setup enables connecting a Compulab SB-UCM-iMX8PLUS development board.
Alternately a board like Raspberry Pi can be connected to test components via development connectors.
Not all the 909 connectors will be mounted on the 801 production bridge board that mounts the i.MX8 board.

- Some of the UCM-iMX8M-Plus carrier board interface pins are multifunctional. Up to 4 functions (ALT modes) are accessible through each multifunctional pin.
- All of the UCM-iMX8M-Plus digital interfaces operate at 3.3V voltage levels unless noted otherwise.
- NOTE: RGMII ENET1 signals operate at 1.8V voltage level
- NOTE: SD/SDIO port #2 can be configured to operate at 3.3V or 1.8V voltage levels. Voltage level is controlled by SoC pin GPIO1_IO04.

TODO
- Check if the 22 pin connectors can be bidirectional
- Signal voltage PD Controller?
- Camera modules are signal voltage 1.8V
- Review if camera 1.8V, 2.8V should come from camera input connector or power connector.
- Dynamic Voltage/Frequency Design options?
- Evaluate the need for additional pinouts from TPS65982 (TPS PD Controller Dev PSIL091B(002).PDF)

![Ziloo Bridge Board 909](./ziloo-bridge-909.png)


## USB Power

If one of the USB-C connectors supplies power it is managed by the USB PD Controller circuit and routed to 
the 10-pin Power Connnector as VIN.

The power connector sends the power from USB-C connectors away from the board
to be used and sent back as regulated 5V.
 
The regulated 5V is used to supply attached USB devices that do not themselves provide power.
The regulated 5V is also downregulated to 3V3, 2V8 and 1V8.

The bridge board is powered via 5V from the 10-pin Power connector, and its downregulated variants. 


#### Power supply TI chipset

TPS65982 USB Type-C® and USB PD Controller, Power Switch, and High-Speed Multiplexer

The TPS65982 device is a stand-alone USB Type-C and Power Delivery (PD) controller providing cable- plug and orientation detection at the USB Type- C connector. Upon cable detection, the TPS65982 device communicates on the CC wire using the USB PD protocol. After successful USB PD negotiation is complete, the TPS65982 enables the appropriate power path and configures alternate mode settings for internal and (optional) external multiplexers.

![Wiring of TPS65988 from datasheet](../datasheets/USB/ref-TPS65988-diagram.png)

A minimal version of this setup should be placed on the 909 to handle power. I.E. No TUSB1044

The 10 pin power connector can be used to test the chipset and USB devices attached.


#### Handling USB Connectors

The two USB ports may power the board. The powering is negotiated and handled by by TPS65988 (in future TPS65994AE).
They also deliver data lanes

Power regulators receive power from USB connectors and supply the 12V & 5V power for development carrier board.
The USB-C connectors can power the carrier board 12V by upregulating, which would be done on the In-Between board.



## 8.1 Carrier Board Design Guidelines

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


## Connectors

Connectors placed on the board are,

- 2 * [Molex 22PIN 0.5mm pitch 54548-2271](https://www.molex.com/molex/products/part-detail/ffc_fpc_connectors/0545482271)
- 2 * [I-PEX 30PIN 0.4mm pitch 20525-030E-02](https://www.i-pex.com/product/cabline-ca)
- 2 * [Hirose USB-C CX80B1-24P](https://www.hirose.com/product/p/CL0480-0625-0-00)
- 1 * [TE Connectivity 45PIN 0.3MM 571-4-2328724-5 FPC 3-2328724-5](https://www.te.com/usa-en/product-4-2328724-5.html) $0.41
- 2 * [Hirose DF40C-34DS-0.4V](https://www.hirose.com/en/product/p/CL0684-4023-0-51) ([Mouser](https://www.mouser.ch/ProductDetail/Hirose-Connector/DF40C-34DS-04V51?qs=vcbW%252B4%252BSTIpg26DsEbj1iQ%3D%3D))

The two 100 pin Hirose connectors are not mounted but are in 3D design for reference. It will connect the MCU board on the 801.



### Wiring the connectors within the board

The 22 pin connectors are connected directly to the equivalent lines on the 30 pins.
The CSI lanes on 34 pins connector is connected directly to the equivalent lines on the 30 pins.
This assumes that a camera is connected to either a 34 pins connector or a 22 pins connector, not both.

  
The data lines from the two USB-C connectors are connected to the equivalent lines on the T-USB direct connector.
The Power pins on USB-C connectors go to the TPS65988 as well as VIN on 10 pins Connector.
TPS65988 is fed 5V and 3V3 from the 10 pins Connector.

GND connected from everywhere as normal.

If power isn't connected over the USB-C plugs, and is power is not supplied by the 10-pin Power connector,
the camera modules should be powered over the MIPI CSI connectors.
In this case it should be possible to use either the 22 pin connectors or the 30 pin connectors for inputting
the signal and power. This means that the 22 pin connectors can be used to input or output MIPI CSI lanes.

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



### Conencting the SB-UCM-iMX8PLUS carrier board

![SB-UCM-iMX8PLUS](../refs/SB-UCMIMX8PLUS-carrier-board.jpg)

For further details see [Product Page](https://www.compulab.com/products/carrier-boards/sb-ucmimx8plus-carrier-board/#diagram).

- 2 * I-PEX connector directly between UCM carrier board and bridge board
- 45 pins connected to Inbetween breakout boards
- 10 pins power connector to Inbetween breakout boards
- USB-C connector to Inbetween breakout boards
- USB-A connector to Inbetween breakout boards
- HDMI female to Inbetween breakout boards



## USB-C to USB-C connector mapping

Two USB-C connectors are arranged in a T shape and the normal way to use it is with a combined connector
attached. This means that the wires will normally be connected in a particular orientation. The system
takes advantage of this by detecting when both USBs are connected in the normal arrangement.

:[T-USB Connector Mapping](../pinouts/T-USB_WITH_DIRECT_CONNECTOR_PINOUT.md)


## Board Power 10 pins Connector

:[10 pins Board Power Connector](../pinouts/BOARD_POWER_CONNECTOR.md)


## T-USB direct connector

This connector(only on the 909 model) enables experimentation with alternate modes and directional pins.

:[45 pins T-USB direct connector](../pinouts/T-USB_DIRECT_CONNECTOR.md)


### Camera breakout connector

These connectors will not normally be mounted, but instead be breakout throughholes.

The two breakouts are spaced 58.42mm (22 * 2.54mm)

:[10 pin Camera breakout connector](../pinouts/CAMERA_BREAKOUT_CONNECTOR.md)





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

