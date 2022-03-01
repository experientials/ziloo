# T-USB connector

The connector is a combination of two USB Type C connectors laid out in a T shape. They can be connected individually as USB Host and USB PC/Power (OTG), or by a combined connector. 

## Components

- 2 * [Hirose USB-C CX80B1-24P](https://www.hirose.com/product/p/CL0480-0625-0-00)
- 1 * [Hirose DF40C-60DS-0.4V](https://www.hirose.com/product/p/CL0684-4004-6-51). [Mouser](https://www.mouser.ch/ProductDetail/Hirose-Connector/DF40C-60DS-04V51?qs=sGAEpiMZZMthaSLPVp%252B4arwMDsgRiqOOXgXHi43jN1w%3D) [JLCPCB part](https://jlcpcb.com/parts/componentSearch?isSearch=true&searchTxt=DF40C-60DS-0.4V)
- 1 * [DF40C-60DP-0.4V]() [JLCPCB part](https://jlcpcb.com/parts/componentSearch?isSearch=true&searchTxt=DF40C-60DP-0.4V)
- 1 * [TPS65988](https://www.ti.com/product/TPS65988?keyMatch=TPS65988&tisearch=search-everything&usecase=GPN) Dual Port USB Type-C® and USB PD Controller, Power Switch, and High-Speed Multiplexer. [Mouser](https://www.mouser.ch/ProductDetail/Texas-Instruments/TPS65988DJRSHR?qs=sGAEpiMZZMv0NwlthflBiyrCPYKWtEb9w8lmLVKGFHI%3D)
- 2 * [HD3SS460RNHR](https://www.ti.com/product/HD3SS460?keyMatch=HD3SS460&tisearch=search-everything&usecase=GPN) 4 x 6 Channels USB Type-C Alternate Mode MUX. Connected to T-USB Host. [Mouser](https://www.mouser.ch/new/texas-instruments/ti-hd3ss460-switch/). [Dock Eval Kit](https://www.mouser.ch/ProductDetail/Texas-Instruments/USB-CTM-MINIDK-EVM?qs=vcbl%252BK4rRletdX9FWp9J9A%3D%3D) [JLCPCB part](https://jlcpcb.com/parts/componentSearch?isSearch=true&searchTxt=DF40C-60DS-0.4V)


## USB Host

The Host mode connector is the vertical stem of the T. 
The USB Host connector can be connected to a dedicated Control and Connectivity module. This module enables
software updates and configuration over Bluetooth via a Mobile App. It also manages awakeness and provides additional environment sensors. 
The USB 2.0 lines can connect to mouse and keyboard.
Alternately it can be used as a general USB 3.0 connection or as Display Port in alternate mode.
This is provided by converting LVDS to Display Port.
The connector can also supply 5V power to the board.


## USB PC/Power (OTG)

The OTG connector is the horizontal bar of the T.
Using OTG mode the connector can be used as a USB device.
The USB OTG connector allows you to use Ziloo as a traditional WebCam using a PC/Mac or Mobile Phone.
In alternate mode is still undefined, it could provide 2 lanes of UART and 2 lanes of I2C.
The connector can also supply 5V power to the board.

* LVDS / MIPI DSI
* [HDMI Alternate Mode for USB Type-C](https://en.wikipedia.org/wiki/HDMI#HDMI_Alternate_Mode_for_USB_Type-C) - [SuperUser info](https://superuser.com/a/1193853)


## Using T-USB Cable

When connecting with a dedicated cable the in-built resistors switches the connection to allow more signals.
The resistors are connected to CC pins to signal the T-USB Extended mode. 

The CC pins can be used to enable alternate T-USB cables for different connections such as,

In extended mode the DX lines provide two additions signals for UART2 & UART4 debug lines.
DX+ DX- pins are used for debugging connections. Re: Serial Debug console UART2 & 4.


TODO Scenarios

* USB 2.0 switching & debug chipset with debug breakout
* Power + Bluetooth/Controller + HDMI Display
* Power + Webcam
* Power + Bluetooth/Controller + Ethernet
* Power + Bluetooth/Controller + Ethernet + HDMI Display
* USB Gadget Ethernet
* USB Gadget Audio
* Alt. Mode UART / I2C


TODO Visual diagram


* Ethernet RX/TX  (4 pins)
* HDMI RX/TX (4 pins)
* Sensor I3C / I2C for Cameras/ToF
* [UG233: USB Type-C Reference Design User's Guide](./datasheets/UG233-USB-Design-Guide.pdf)
* [USB-CTM to DisplayPort Active Cable Reference Design](./datasheets/tidudr0.pdf)
* [Alternate Mode for USB Type-CTM: Going beyond USB](./datasheets/slly021.pdf)
* [STEVAL-USBC2DP USB Type-CTM to DisplayPortTM adapter](./datasheets/dm00474479-stevalusbc2dp-usb-typec-to-displayport-adapter-stmicroelectronics.pdf)


From 5.2.1

External regulator control and power management
UCM-iMX8M-Plus supports carrier board power supply control by means of two dedicated output signals. Both signals are derived from the i.MX8M Plus SoC. The logic that controls both signals is supplied by the i.MX8M Plus SoC SNVS power rail.
The PMIC_STBY_REQ output can be used to signal the carrier board power supply that UCM- iMX8M-Plus is in ‘standby’ or ‘OFF’ mode. Utilizing the external regulator control signals enables carrier board power management functionality.
Please refer to the i.MX8M Plus Reference manual for additional details. The table below summarizes the external regulator control signals.
Table 38 External regulator control signals
     Signal Name
PMIC_STBY_REQ PMIC_ON_REQ PWRBTN
5.3 Reset
Pin # Type
P1-66 O P1-68 O P2-64 I
Description
When the processor enters SUSPEND mode, it will assert this signal.
Active high power-up request output from i.MX8M Plus SoC.
Pulled-Up Active low ON/OFF signal (designed for an ONOFF switch).
Availability
Always available Always available Always available
                    SYS_RST_PMIC signal is the main system reset input. Driving a valid logic zero invokes a global reset that affects every module on UCM-iMX8M-Plus. Please refer to the i.MX8M Plus Reference manual for additional details.
Table 39 Reset signals
Signal Name Pin # Type Description
SYS_RST_PMIC P1-2 I Active Low cold reset input signal. Should be used as main system reset

Availability
Always available


### Power ratings

- TPS65988 can supply 3A, as 5V / 9V / 12V.
- PCA9450C can handle 3A (or dual-phase 6A)
- USB-C is max 3A @ 5V

VSOM and GND are using 10 pins each totalling at 3A.
VCC_RTC can max provide 500mA. NVCC_SNVS_1P8  1.8V


### Combined T-USB control I/O Expander

Expander #3 combines control signals.

:[Combined T-USB control I/O Expander](../pinouts/I2C_EXPANDER_3.md)

### DF40 50 pin connectors

:[DF40 50 pin connectors](../pinouts/T-USB_50_PINS_CONNECTORS.md)








