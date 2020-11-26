To develop install the following dependencies

    pip3 install rshell esptool
    

- [Raspberry Pi ext4 to f2fs](http://whitehorseplanet.org/gate/topics/documentation/public/howto_ext4_to_f2fs_root_partition_raspi.html)


## Raspberry Pi 4

The continuos delivery and integration testing platform is Raspberry Pi 4. To get flexibility in connectivity the compute module is used.
It is booted from an SSD over PCI or USB. This leaves the SD card available for writing new cards as part of build/tooling.
For automated builds simulated video devices are used, but for ad-hoc testing a set of stereo cameras are used.

Components include,

* [Raspberry Pi Compute Module 4 IO Board With PoE Feature (Type B), for all Variants of CM4](https://www.waveshare.com/compute-module-4-poe-board-b.htm?___SID=U)
* [IMX219-83 Stereo Camera, 8MP Binocular Camera Module, Depth Vision](https://www.waveshare.com/imx219-83-stereo-camera.htm)
* [Raspberry Pi Compute Module 4, 2GB / No EMMC / Wireless CM4102000](https://www.waveshare.com/product/raspberry-pi/boards-kits/compute-module-4-cat/compute-module-4.htm?sku=18788)
