# M.2 Key B LoRa SSD module

This module implements an expansion module with an M.2 Key B 2030 shape. It uses existing modules to simplify development.


## Components

- [Murata LPWA LoRaWAN CMWX1ZZABZ-093](https://www.murata.com/products/connectivitymodule/lpwa/overview/lineup/type-abz-093) needs 3.6V
- [Murata LPWA LoRaWAN 1SJ LBAA0QB1SJ-296](https://www.murata.com/en-global/products/connectivitymodule/lpwa/overview/lineup/type-1sj-296) - [Mouser](https://www.mouser.ch/ProductDetail/Murata-Electronics/LBAA0QB1SJ-296?qs=bAKSY%2FctAC4zFVZan%252ByjLw%3D%3D) runs on 3.3V


The Murata module uses UART as host interface


An SSD could be combined with remote monitoring, supervision and remote control.
It would extend the features available to the SoM and.

- SSD storage
- LoRa/BT + antenna COEX
- Wake up the system triggered by message received
- Instruct expander over I2C to shut down, restart, wake/suspend the SoM.
- Send commands

Stem SDA
Stem SCL
Stem INT
Sensor SDA
Sensor SCL
SYS SDA
SYS SCL
SPICLK
MOSI
MISO

LoRa module could be $25 Kyocera ETH-LORA-M-AX-01 or Murata CMWX1ZZABZ.
LoRa needs UART, SPI, I2C. 
BLE needs UART.

LoRa Symphony Link may be able to offer [bug-fixes over the air](https://www.link-labs.com/blog/sigfox-vs-lora )

LTE-M is an alternative. [What is LTE-M and How Does it Compare to NB-IOT](https://www.link-labs.com/blog/what-is-lte-m). [4G Mall](https://www.4gltemall.com/m2m-lte-module.html)


- [MobileTek N20B GNSS Module](https://www.4gltemall.com/mobiletek-n20b.html)
- [Quectel L76B GNSS Module](https://www.4gltemall.com/quectel-l76b-gnss-module.html) - [Product page](https://www.quectel.com/ProductDownload/L76B.html)
- [Quectel LG77L GNSS Module](https://www.quectel.com/product/gnss-lg77l-series) - [Datasheet](https://www.quectel.com/wp-content/uploads/2021/06/Quectel_LG77L_GNSS_Specification_V1.3.pdf) - 
- [ED20 2G+GNSS Module, Based on MT2503](https://www.electrodragon.com/product/ed20-gsmgprsgnss-module/)


### Fanstel Supplier [site](fanstel.com)

Fanstel makes OEM m.2 modules with wireless comms. LoRa etc.

M262X40F with BLE + LoRa (nRF5340 + LR62XE)

The modules are too wide for Ziloo. 3042 form factors





[m.2 Advantech Design Guide](https://advdownload.advantech.com/productfile/Downloadfile5/1-1KJUZ5Q/M2%20COM%20Board%20Design%20Guide%20V1.1.pdf)

- UART, I2S and SDIO is 3V3
- 

[Converting M.2 key M to B+M missing config pull up](https://www.youtube.com/watch?v=E1TO38nsMvY)

