# IoT Raspberry PI Documentation

## Installation

### Raspbian
Raspbian is the Foundation’s official supported operating system and the best bet if you want the best hardware support.
To install Raspbian download the current image from the download page:
https://www.raspberrypi.org/downloads/raspbian/

**Note**: We are recommend to use the Full Desktop image

After you downloaded the Raspbian image to through the installation guide for you specific plattform:
* **Linux**: https://www.raspberrypi.org/documentation/installation/installing-images/linux.md
* **Mac**: https://www.raspberrypi.org/documentation/installation/installing-images/mac.md
* **Windows**: https://www.raspberrypi.org/documentation/installation/installing-images/windows.md

Before you eject the SD Card just add the following line to the ```/config.txt```
```
dtoverlay=pi3-miniuart-bt
```
This command will enable the login via the ```UART-Interface``` with a console/TTL cable

## Configuration

### Basic Settings
To enabled the basic settings just type in:
```
sudo raspi-config
```

For a basic configuration you need to set the following options:
* [1] Expand Filesystem: Yes
* [6] Enable Camera: Enable
* [9] Advanced Options -> [A2] Hostname: ```raspberrypiXX``` (e.g.) ```raspberrypi09```
* [9] Advanced Options -> [A6] I2C: Enable the ```ARM I2C Interface``` and the ```I2C Kernel Modul```
* [9] Advanced Options -> [AA] 1-Wire: Enable

After the configuration the is a reboot needed: ```sudo shutdown -r now```.

### Install all of the needed sources
To install all of the needed sources, libraries and package just execute the ```install.sh``` script in the root directory of the git repo.
```
sudo ./install.sh
```

### Testing I2C Ports
To check everything is working just run the ```sudo i2cdetect -y 1``` command in the terminal.
If there are some error's just google or check out the [Adafruit Guide](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c) to enable the i2c ports on the Raspberry PI.


### Desktop
By default the Desktop is enable, to boot without the desktop just run the following in the terminal:
```
sudo raspi-config
```
Go to boot options and change to the needed option and reboot.

## Camera

There are few steps needed to use the Raspberry Pi Camera

### Installation

Open the Raspberry Pi configuration with ```sudo raspi-config``` and enable the camera. If you have the v1 version of the camera you are good to go and can skip to the next point. For the [v2](https://www.raspberrypi.org/blog/new-8-megapixel-camera-board-sale-25/) version please continue with the following steps:

### Using the camera

There are detailed information about the camera usage with [python](https://www.raspberrypi.org/documentation/usage/camera/python/README.md) and [bash](https://www.raspberrypi.org/documentation/usage/camera/raspicam/README.md) on the official raspberry pi website: https://www.raspberrypi.org/help/camera-module-setup/
