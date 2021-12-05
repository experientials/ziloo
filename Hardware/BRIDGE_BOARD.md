# Bridge Board

The bridge board connects two camera modules, external connectors and i.MX8M Plus module.

Connectors placed on the board are,

* [Hirose DF40C-100DS-0.4V](https://www.hirose.com/en/product/p/CL0684-4033-4-51)
* [Hirose CX80B1-24P](https://www.hirose.com/product/p/CL0480-0625-0-00)
* [Hirose microSD DM3BT-DSF-PEJS](https://www.hirose.com/product/p/CL0609-0029-9-00)
* [TE Connectivity 45PIN 0.3MM 571-4-2328724-5 FPC 3-2328724-5](https://www.te.com/usa-en/product-4-2328724-5.html) $0.41
* [Hirose DF40C-34DS-0.4V](https://www.hirose.com/en/product/p/CL0684-4024-3-51) ([Mouser](https://www.mouser.ch/ProductDetail/Hirose-Connector/DF40C-34DS-04V51?qs=vcbW%252B4%252BSTIpg26DsEbj1iQ%3D%3D))
* [Amphenol M.2 Connector Key B 10128787](https://www.amphenol-icc.com/pcie-m-2-10128787001rlf.html)
 * [CR2450 battery holder BAT-HLD-006-SMT](https://www.mouser.ch/ProductDetail/Linx-Technologies/BAT-HLD-006-SMT?qs=TuK3vfAjtkUyTQHMSqIP6A%3D%3D)


## Camera Module 201 row connectors

These two connectors have identical pinouts and connect the bridge board to two Camera Modules.

:[Camera Module 201 connector](./CAMERA_MODULE_CONNECTOR_PINOUT.md)



## Camera Module Development and testing

The brige board can be used to test Camera Modules. Connections from the image sensors are connected to the RPi Zero 22pin connector.
This allows the bridge board to be connected to a [Raspberry Pi CM 4 IO Board](https://www.waveshare.com/compute-module-4-io-board.htm) or [Tinker Edge R](https://tinker-board.asus.com/product/tinker-edge-r.html) for testing.

The 3.3V pin can go both ways depending on setup.

1) When the MCU daughter board is mounted alternate cameras can be connected to the 15 pin connectors instead of to the Camera
Module connectors. This means that the board must supply power out on the 3.3V pin and receive power over the USB plug

Pin #	Name	Description
1	GND	Ground
2	CAM_D0_N	MIPI Data Lane 0 Negative
3	CAM_D0_P	MIPI Data Lane 0 Positive
4	GND	Ground
5	CAM_D1_N	MIPI Data Lane 1 Negative
6	CAM_D1_P	MIPI Data Lane 1 Positive
7	GND	Ground
8	CAM_CK_N	MIPI Clock Lane Negative
9	CAM_CK_P	MIPI Clock Lane Positive
10	GND	Ground
11	CAM_IO0	Power Enable
12	CAM_IO1	LED Indicator
13	CAM_SCL	I2C SCL
14	CAM_SDA	I2C SDA
15	CAM_3V3	3.3V Power Input

For development and testing there are additional optional connectors,

TODO 22 pins

* 2 * RPi compatible [TE Connectivity 15pin 1mm FPC 1-84952-5](https://www.te.com/usa-en/product-1-84952-5.html)
* [TE 45 pins Wire-to-Board FPC 0.3 4-2328724-5](https://www.te.com/usa-en/product-4-2328724-5.html) ([Mouser](https://eu.mouser.com/ProductDetail/TE-Connectivity/4-2328724-5?qs=w%2Fv1CP2dgqow3y3efq3sig%3D%3D)) $0.41

MIPI DSI display output


## NVIDIA compatible connector

20525-030E-02

https://www.i-pex.com/product/cabline-ca
0.4mm pitch
30 pins

Reference camera module:

https://www.e-consystems.com/4k-autofocus-camera-for-variscite-imx8.asp



## I2C Allocation

2. Is system I2C with EEPROM / RTC.



## Other notes


Inspiration from https://www.waveshare.com/wiki/IMX219-83_Stereo_Camera?spm=a2g0o.detail.1000023.2.296d4832DZoKOX

Use accelerometer 
ICM20948:
Accelerometer:
Resolution: 16-bit
Measuring Range (configurable): ±2, ±4, ±8, ±16g
Operating Current: 68.9uA
Gyroscope:
Resolution: 16-bit
Measuring Range (configurable): ±250, ±500, ±1000, ±2000°/sec
Operating Current: 1.23mA
Magnetometer:
Resolution: 16-bit
Measuring Range: ±4900μT
Operating Current: 90uA


Development breakouts (bigger version more connectors)

- 24 pins MIPI CSI ?
- 40 pins for MIPI CSI cams

Alternative Eye connectivity

* [DF40GL-44DP-0.4V(58)](https://www.mouser.ch/ProductDetail/Hirose-Connector/DF40GL-44DP-04V58?qs=vcbW%252B4%252BSTIqnxpqC5YNomg%3D%3D)
* [DF40GL-44DS-0.4V(58)](https://www.mouser.ch/ProductDetail/Hirose-Connector/DF40GL-44DS-04V58?qs=vcbW%252B4%252BSTIrCOhN%252ByyWFhA%3D%3D)


Mating with

* [Hirose DF50C-100DP-0.4V](https://www.hirose.com/product/p/CL0684-4032-1-51#)
* [Hirose DF40C-34DP-0.4V(51) for Eye]() - [Mouser](https://www.mouser.ch/ProductDetail/Hirose-Connector/DF40C-34DP-04V51?qs=vcbW%252B4%252BSTIrNaWXujOGbOA%3D%3D)

Not used:


* [MAX14998ETO+T IC DISPLAY PORT MUX 4CH 42TQFN](https://www.digikey.com/en/products/detail/maxim-integrated/MAX14998ETO-T/2238703)



Key B
PCIe x2
SATA
USB 2.0 / 3.0
AUDIO
UIM HSIC SSIC I2C SMBus

Alternate USB 2 pinouts / gpio ?

Allow 30mm wide, 42mm long module (thickness S3 ? = 1.5mm on top)


M.2 Key B - LoRA
LR62E, Semtech SX1262 module
https://www.fanstel.com/lr1262


WiFi M.2 B key module 2242 2230 MT7612U 
https://www.asiarf.com/shop/hot-sales/wifi-m-2-b-key-module-2242-2230-mt7612u-11ac-2x2-867-mbps-m27612-bu3/

M.2 Key B - Wavlink AX3000 M.2 WiFi 6 3000Mbps WiFi Card Intel AX200 WiFi / BT 5.1
https://www.newegg.com/wavlink-690a5d-usb-3-0/p/0XM-00B5-00052?Description=m.2%20wifi&cm_re=m.2_wifi-_-0XM-00B5-00052-_-Product&quicklink=true

M.2 Key B - Dell OEM Wireless 5808E DW5808E M.2 Mobile Broadband 4G LTE WWAN Card 4GP3D
https://www.newegg.com/p/0XM-005R-000P1?Description=m.2%20lte&cm_re=m.2_lte-_-0XM-005R-000P1-_-Product


SMB Asembly China
https://www.nextpcb.com/

SMB Assembly Europe
https://www.smtlowcost.com