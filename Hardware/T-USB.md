# T-USB connector

The connector is a combination of two USB Type C connectors laid out in a T shape. They can be connected individually as USB Host and USB PC/Power (OTG). 

## USB Host

The USB Host connector can be connected to a dedicated Control and Connectivity module. This module enables
software updates and configuration over Bluetooth via a Mobile App. It also manages awakeness and provides additional environment sensors.

## USB PC/Power (OTG)

The USB OTG connector allows you to use Ziloo as a traditional WebCam using a PC/Mac or Mobile Phone.
It is also the port for supplying 5V power.


## Using T-USB Cable

When connecting with a dedicated cable the in-built resistors switches the connection to allow more signals.
The resistors are connected to CC pins to signal the T-USB Alternate mode. 

The CC pins can be used to enable alternate T-USB cables for different connections such as,

* LVDS / MIPI DSI
* [HDMI Alternate Mode for USB Type-C](https://en.wikipedia.org/wiki/HDMI#HDMI_Alternate_Mode_for_USB_Type-C) - [SuperUser info](https://superuser.com/a/1193853)
* Ethernet

Difference resistance levels or something similar.


TODO
DX+ DX- pins are used for debugging connections. Re: Serial Debug console UART2 & 4.


TODO Scenarios

* Power + Bluetooth/Controller + HDMI Display
* Power + Webcam
* Power + Bluetooth/Controller + Ethernet
* Power + Bluetooth/Controller + Ethernet + HDMI Display


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