To develop install the following dependencies

    pip3 install rshell esptool
    

- [Raspberry Pi ext4 to f2fs](http://whitehorseplanet.org/gate/topics/documentation/public/howto_ext4_to_f2fs_root_partition_raspi.html)

## Development boards note

- [Download images for I-Pi SMARC IMX8M Plus](https://www.ipi.wiki/pages/downloads-imx8mplus)
- [How to use wic for make sd card](https://community.nxp.com/t5/i-MX-Processors/Yocto-i-MX28-How-to-use-wic-for-make-sd-card/m-p/758764)


```sh
gunzip -c <IMAGE>.wic.gz | sudo dd of=/dev/sdX bs=1M  iflag=fullblock oflag=direct conv=fsync
```

Or use Balena Etcher


## Development Environment

1. [Visual Studio Code](https://code.visualstudio.com/) (1.33.1)
2. Visual Studio Code Extension: [C/C++](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools) (0.22.1)
3. Visual Studio Code Extension: [CMake Tools](https://marketplace.visualstudio.com/items?itemName=vector-of-bool.cmake-tools) (1.1.3)
4. Visual Studio Code Extension: [Cortex-Debug](https://marketplace.visualstudio.com/items?itemName=marus25.cortex-debug) (0.2.3)
5. [SEGGER J-Link](https://www.segger.com/downloads/jlink#J-LinkSoftwareAndDocumentationPack)
6. CMakeLists.txt
7. cmake-kits.json
8. launch.json
9. settings.json


[USING CMAKE FOR NORDIC NRF52 PROJECTS](https://www.nrbtech.io/blog/2020/1/4/using-cmake-for-nordic-nrf52-projects).

[how to install gcc-arm-none-eabi at Mojave MacOS
](https://stackoverflow.com/questions/59861085/how-to-install-gcc-arm-none-eabi-at-mojave-macos).

[How to Set up the Open Source IDE for nRF5x Development](https://www.polidea.com/blog/how-to-set-up-the-open-source-ide-for-nrf5x-development/).


## Raspberry Pi 4

The continuos delivery and integration testing platform is Raspberry Pi 4. To get flexibility in connectivity the compute module is used.
It is booted from an SSD over PCI or USB. This leaves the SD card available for writing new cards as part of build/tooling.
For automated builds simulated video devices are used, but for ad-hoc testing a set of stereo cameras are used.

Components include,

* [Raspberry Pi Compute Module 4 IO Board With PoE Feature (Type B), for all Variants of CM4](https://www.waveshare.com/compute-module-4-poe-board-b.htm?___SID=U)
* [IMX219-83 Stereo Camera, 8MP Binocular Camera Module, Depth Vision](https://www.waveshare.com/imx219-83-stereo-camera.htm)
* [Raspberry Pi Compute Module 4, 2GB / No EMMC / Wireless CM4102000](https://www.waveshare.com/product/raspberry-pi/boards-kits/compute-module-4-cat/compute-module-4.htm?sku=18788)
* [Compute module devboard support cameras](https://www.waveshare.com/wiki/CM4-IO-BASE-A)


Test camera0:

```
sudo raspivid -t 0 -cs 0
```

Test camera1:

```
sudo raspivid -t 0 -cs 1
```
