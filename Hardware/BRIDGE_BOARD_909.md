# Bridge Board 909

The 909 is a Bridge Board version made for testing and experiementation with the Ziloo attachments without attaching
the i.MX8 board. The setup enables connecting a Compulab SB-UCM-iMX8PLUS development board.
Alternately a board like Raspberry Pi can be connected to test components via development connectors.
Not all these connectors will be mounted on the 801 production bridge board that mounts the i.MX8 board.


## Connectors

- 2 * RPI 22 pin connectors
- 2 * NVIDIA 30 pin connectors
- 2 * Hirose 34 pin connectors
- 2 * USB-C connectors
- 45 pin extras connector

The two 100 pin Hirose connectors are not mounted but are in 3D design for reference. It will connect the MCU board on the 801.


### Soldering isles

Soldering iles allows the board connections to be tweaked by,

- Connecting power to pins on individual camera connectors
- Connecting I2C busses together
- Connecting I2S busses together



### Conencting the SB-UCM-iMX8PLUS development board

- Ethernet connector 2
- 2 * I-PEX connector
- USB-C connector to OTG
- USB-A connector to Host
- HDMI female (in revision B)
- Pins to extras connector

Common ground/3V3/5V shared? 
Power board over USB ?


Power supply TI chipset
TPS65982 USB Type-C® and USB PD Controller, Power Switch, and High-Speed Multiplexer

The TPS65982 device is a stand-alone USB Type-C and Power Delivery (PD) controller providing cable- plug and orientation detection at the USB Type- C connector. Upon cable detection, the TPS65982 device communicates on the CC wire using the USB PD protocol. After successful USB PD negotiation is complete, the TPS65982 enables the appropriate power path and configures alternate mode settings for internal and (optional) external multiplexers.


## Connector layouts

### USB-C to USB-C connector mapping

Two USB-C connectors are arranged in a T shape and the normal way to use it is with a combined connector
attached. This means that the wires will normally be connected in a particular orientation. The system
takes advantage of this by detecting when both USBs are connected in the normal arrangement.

In revision B the Host connector is alternately used to carry HDMI instead of connecting to 
Bluetooth/Wifi connectivity.

:[T-USB Connector Mapping](./T-USB_CONNECTOR_PINOUT.md)


USB connectors

CS80B1-24P



### Extras connector

Pins from USB

USB-H is otherwise connected to USB #2
USB-O is otherwise connected to USB #1

| 1   | GND       |
| 2   | USB-H TX2+  | Host alt TX+
| 3   | USB-H TX2-  | Host alt TX-
| 4   | GND       |
| 5   | USB-H SBU1  | Host alt SBU1
| 6   | USB-H SBU2  | Host alt SBU2
| 7   | GND       |
| 8   | USB-H RX1-  | Host alt RX1-
| 9   | USB-H RX1+  | Host alt RX1+
| 10  | GND       |
| 11  | USB-H DX+   | Host alt DX+
| 12  | USB-H DX-   | Host alt DX-
| 13  | GND       |
| 14   | USB-H TX2+  | Host alt TX+
| 15   | USB-H TX2-  | Host alt TX-
| 16   | GND       |
| 17   | USB-H SBU1  | Host alt SBU1
| 18   | USB-H SBU2  | Host alt SBU2
| 19   | GND       |
| 20   | USB-H RX1-  | Host alt RX1-
| 21   | USB-H RX1+  | Host alt RX1+
| 22  | GND       |
| 23  | USB-H DX+   | Host alt DX+
| 24  | USB-H DX-   | Host alt DX-
| 25  | GND       |
| 26  | USB-O TX2+  | OTG alt TX+
| 27  | USB-O TX2-  | OTG alt TX-
| 28  | GND       |
| 29  | USB-O SBU1  | OTG alt SBU1
| 30  | USB-O SBU2  | OTG alt SBU2
| 31  | GND       |
| 32  | USB-O RX1-  | OTG alt RX1-
| 33  | USB-O RX1+  | OTG alt RX1+
| 34  | GND       |
| 35  | USB-O DX+   | OTG alt DX+
| 36  | USB-O DX-   | OTG alt DX-
| 37  | GND       |


### HDMI connector mapping (future rev B)

The HDMI signal from the i.MX8 board is mapped to USB-C. While providing HDMI Ziloo cannot be connected
to


### USB4 support (future rev C)

* Use Texas Instruments TPS65994AD to route thunderbolt

USB Interface IC Dual port USB Type-C and USB PD controller with integrated source power switches 48-VQFN -40 to 125

[Temporary stop for Thunderbolt 4 and USB 4 on Intel’s Tiger Lake?](https://www.igorslab.de/en/goes-with-intel-for-tiger-lake-and-thunderbolt-4-bald-the-lights-out-what-chip-shortage-really-means-exclusively/)


### RPI FPC 22 pins

Raspberry Pi connectors

- 1-7342485-5  TE Connectivity  15 pins vertical Pi Board A/B
- 54548-2271   Molex 22 pins  Right angle Pi Zero & Compute module
- SFW15R-2STE1LF  Amphenol FCI 15 pins Right angle Camera Module



| Pin | Code       | Type     | Details                              | Voltage |
|-----|------------|----------|--------------------------------------|---------|
| 1   |	GND        | Power    | Ground                               |      |
| 2   |	CAM_D0_N   | Data     | MIPI Data Lane 0 Negative            |      |
| 3   |	CAM_D0_P   | Data     | MIPI Data Lane 0 Positive            |      |
| 4   |	GND        | Power    | Ground                               |      |
| 5   |	CAM_D1_N   | Data     | MIPI Data Lane 1 Negative            |      |
| 6   |	CAM_D1_P   | Data     | MIPI Data Lane 1 Positive            |      |
| 7   |	GND        | Power    | Ground                               |      |
| 8   |	CAM_CK_N   | Data     | MIPI Clock Lane Negative             |      |
| 9   |	CAM_CK_P   | Data     | MIPI Clock Lane Positive             |      |
| 10  |	GND        | Power    | Ground                               |      |
| 11  |	CAM_D2_N   | Data     | MIPI Data Lane 2 Negative            |      |
| 12  |	CAM_D2_P   | Data     | MIPI Data Lane 2 Positive            |      |
| 13  |	GND        | Power    | Ground                               |      |
| 14  |	CAM_D3_N   | Data     | MIPI Data Lane 3 Negative            |      |
| 15  |	CAM_D3_P   | Data     | MIPI Data Lane 3 Positive            |      |
| 16  |	GND        | Power    | Ground                               |      |
| 17  |	CAM_IO0    | Power    | Power Enable                         |      |
| 18  |	CAM_IO1    | LED      | LED Indicator                        |      |
| 19  |	GND        | Power    | Ground                               |      |
| 20  |	SCL        | I2C      | I2C SCL                              |      |
| 21  |	SDA        | I2C      | SCCB serial Interface data IO        |      |                               |      |
| 22  |	VCC        | Power    | 3.3V Power Supply                    |      |
`


### NVIDIA FPC 30 pins

The connector is an [I-PEX type 20525-030E-02](https://www.i-pex.com/product/cabline-ca) with 0.4mm pitch & 30 pins.
Data pins are 1.8V level.


| Pin | Code       | Details                              |
|-----|------------|--------------------------------------|
| 1   | CAM_3V3	   | 3.3V Power Input                     |
| 2   | CAM_3V3    |                                      |
| 3   | CAM_1V8	   | 1.8V Power Input                     |
| 4   | GND        |                   |
| 5   | GND        |                   |
| 6   | PWR DWN    |                   |
| 7   | I2C SCL    |                   |
| 8   | I2C SDA    |                   |
| 9   | GND        |                   |
| 10  | CSI D2-    |                   |
| 11  | CSI D2+    |                   |
| 12  | TRIGGER    |                   |
| 13  | MCLK       |                   |
| 14  | Reserved   |                   |
| 15  | CSI D1-    |                   |
| 16  | CSI D1+    |                   |
| 17  | GND        |                   |
| 18  | GND        |                   |
| 19  | CSI D0-    |                   |
| 20  | CSI D0+    |                   |
| 21  | RESET      |                   |
| 22  | GND        |                   |
| 23  | Reserved   |                   |
| 24  | CSI CLK-   |                   |
| 25  | CSI CLK+   |                   |
| 26  | GND        |                   |
| 27  | CSI D3-    |                   |
| 28  | CSI D3+    |                   |
| 29  | Flash      |                   |
| 30  | Reserved   |                   |

Refs
- https://www.leopardimaging.com/product/accessories/cables/faw-1233-03/
- https://www.mouser.com/datasheet/2/233/LI-TX1-CB-6CAM_datasheet-1395894.pdf
- https://connecttech.com/ftp/pdf/ASG006_Spacely.pdf
- https://www.i-pex.com/product/cabline-ca


### Ziloo Camera Module 34 pin connector

**Just to be clear**: All CSI lanes are laid out on one side of the connector with GND between.

:[Camera Module 201 connector](./CAMERA_MODULE_CONNECTOR_PINOUT.md)

