
## 3 pin Battery connector

1. +
2. GND
3. Thermistor

This would be a AMP Connectors 2.0mm surface mounted connector for the embedded battery.
This should be rated at 3A+ to support alternative battery with higher discharge. 
There should be three islands allowing soldering on the battery wires.

TE Connectivity AMP Connectors 2.0mm (4A rated)
[3-292173-3](https://www.mouser.ch/ProductDetail/TE-Connectivity/3-292173-3/?qs=%2Fha2pyFadujfUajo0PC2AYyF1gsMGGMwFqfsq3hzxLc%3D)

JAE Electronics 3mm (3A rated)
[ES9P004VFZR1600](https://www.digikey.com/en/products/detail/jae-electronics/ES9P004VFZR1600/4867379?s=N4IgTCBcDaIKIGUCcAFADGgLANQGIC0AlARgDYMQBdAXyA)


## 12 pin compression connector

2 Molex [6 pin compression connectors](https://www.molex.com/molex/products/part-detail/pcb_headers/0788641001)

1. VSYS
2. VSYS
3. Gut SCL (TX1)
4. Gut SDA (RX1)
5. D+
6. D-
7.
8. SPI SCK (SBU1/SBU2)
9. SPI MISO (TX2)
10. SPI MOSI (RX2)
11. GND
12. GND

## 20 pin Power supply connector 522072033

The battery connector is a direct connection to the internals in the Power Module via 20 pin 1A FFC FPC.
The Molex connectors have 1A current rating, other connectors only have 0.5A current rating.

1. V_SYS 3.5V - 4.4V
2. V_SYS 3.5V - 4.4V
3. V_SYS 3.5V - 4.4V
4. V_CHARGE 4.2V - 5V (Allows MCU board to charge battery)
5. GND
6. Gut SDA (400 KHz)
7. Gut SCL (400 KHz)
8. IRQ Charger
9. SBU1
10. SBU2
11. LEDEN / CHG_STAT (Internal)
12. GND
13. D+
14. D-
15. GND
16. RX+
17. RX-
18. GND
19. TX+
20. TX-

[Easy-On FFC/FPC Connector, 1.00mm Pitch, Slider Series, Vertical, 5.75mm Height, 20 Circuits, Tin-Silver-Bismuth Plating](https://www.molex.com/molex/products/part-detail/ffc_fpc_connectors/0526102034)


## USB-C female socket

Another connector on the top edge of the bottom board will be an USB Type C female connector. 
It will share lines with the underside connections.

The board must have a clear set of isles for cutting the connection between pins on the 20 pin PS connector
and the USB-C connector. When cut it must be possible re-connect the pins by solding the isles together.

![USB-C Pins](./USB-C_pins.png)

Cut/Resolder isles:

14. TX1
15. RX1
16. TX2
17. RX2
18. SBU1
19. SBU2
20. CC
