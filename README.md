re# IoT Raspberry PI Documentation

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

### Connect
There are three different ways to connect to the Raspberry PI:

**Graphic**: You can directly connect the Raspberry Pi to a HDMI display, Keyboard and Mouse.

**SSH**: On every raspberry pi there is a ssh server running. To connect to the rasberry pi just try to run the command ```ssh pi@IP-FOR-YOU-RASPBERRY```. The password for the user ```pi``` is raspberry.

**Console Cable**:
If you want to connect via a Console Cable you need to install the following driver for the **PL2303** USB to TTL Chipset on you local machine: http://www.prolific.com.tw/US/ShowProduct.aspx?pcid=41&showlevel=0041-0041.

On linux and Mac OS X you can run the command ```screen /dev/ttyUSBSerial 115200``` to connect to the Raspberry Pi.
Within Windows you need to download [Putty](http://www.putty.org). You can find the com port by looking in the Ports section of the Windows Device Manager.

For further information you can check out the tutorial from Adafruit: https://learn.adafruit.com/adafruits-raspberry-pi-lesson-5-using-a-console-cable/overview

If everything up and running you need to enable the i2c ports and install the GPIO Python library.

### Enable i2c Ports
To enable the i2c Ports just running the following commands in the Terminal to install the i2c-tools utility.
```
sudo apt-get install python-smbus
sudo apt-get install i2c-tools
```

To enable the i2c Interface and Kernel Modul open the raspbian configuration
```
sudo raspi-configre
```
Go to: ```Advanced Options -> I2C``` and enable the ```ARM I2C Interface``` and the ```I2C Kernel Modul``` by confirming the two questions with yes.

After you enabled the i2c Interface do a ```sudo shutdown -r now``` to restart the Raspberry PI.

### Testing i2c Ports
To check everything is working just run the ```sudo i2cdetect -y 1``` command in the terminal.
If there are some error's just google or check out the [Adafruit Guide](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c) to enable the i2c ports on the Raspberry PI.

### Install GPIO Support
To program the GPIO ports in Python, we need to install a very useful Python 2 library called Rpi.GPIO. This module gives us a simple to use Python library that will let us control the GPIO pins.

Run the following commands to install the library:
```
sudo apt-get update
sudo apt-get install python-dev
sudo apt-get install python-rpi.gpio
```
## Sensor's
With the current setup we provided a bunch of sensor's:
* [DHT22]( https://www.adafruit.com/products/385): The DHT22 is a basic, low-cost **digital temperature** and **humidity sensor**. It uses a capacitive humidity sensor and a thermistor to measure the surrounding air, and spits out a digital signal on the data pin (no analog input pins needed). Its fairly simple to use, but requires careful timing to grab data. The only real **downside of this sensor is you can only get new data from it once every 2 seconds**, so when using our library, sensor readings can be up to 2 seconds old.

* [MTK3339](https://www.adafruit.com/products/746): The MKT3339 is a high-quality **GPS module** that can track up to 22 satellites on 66 channels, has an excellent high-sensitivity receiver (-165 dB tracking!), and a built in antenna. It can do up to 10 location updates a second for high speed, high sensitivity logging or tracking. Power usage is incredibly low, only 20 mA during navigation.

* [TSL2561](https://www.adafruit.com/products/439): The TSL2561 **luminosity sensor** is an advanced digital light sensor, ideal for use in a wide range of light situations. Compared to low cost CdS cells, this sensor is more precise, allowing for exact lux calculations and can be configured for different gain/timing ranges to detect light ranges from up to 0.1 - 40,000+ Lux on the fly. The best part of this sensor is that it contains both **infrared and full spectrum diodes**!

* [L3GD20H / LSM303](https://www.adafruit.com/products/1714): This inertial-measurement-unit combines 2 of the best quality sensors available on the market to give you 9 axes of data: **3 axes of accelerometer data, 3 axes gyroscopic, and 3 axes magnetic (compass)**.

### Using the Sensor's
There are a few different way's to interact with the sensors.

***Localy***:
* **Do it by yourself**: If you are happy and a crazy nerd you can do everything by yourself. The sensors are already connected to the Raspberry PI's GPIO or i2c ports and feel free to develop in any language you would like.
* **Example Python Scripts**: In the ```/home/pi/iot-hackathon``` directory are folders for every sensor. You can check out in the specific example folder (e.g ```/home/pi/iot-hackathon/dht22/example```) some of python scripts to work with the sensor data and get an idea how to interact with the data itself.
* **Local Server**: For each of the sensor there is a local [unix domain socket server](https://en.wikipedia.org/wiki/Unix_domain_socket) running. You can connect **only locally** to the server by connecting to the socket for the sensor (e.g ```/tmp/iot-dht22.sock```). There is also a client example for every sensor in the ```client-server``` directory for the sensor (e.g ``/home/pi/iot-hackathon/dht22/client-server```).

**Note**: For the Remote solution, mentioned below, we are also using the local unix domain socket server. The advantage of this behaviour is that you dont need that start the scripts for every sensor by your self.

***Remote:***
* **MQTT**: If you want to request the sensor data from a remote device directly from the Raspberry PI there is a [RabbitMQ](http://www.rabbitmq.com) server that supports [amqp](https://en.wikipedia.org/wiki/Advanced_Message_Queuing_Protocol) up and running. With this service you have the ability to get real time data from the sensors without develop something on the raspberry itself. For further information check out the [AMQP documentation](AMQP.md).
* **Cloud**: We also push all of the recorded data from all sensors into the cloud. Every second there will be a new record save with all the included data from the sensor and the Raspberry Pi pushes the data to the cloud every 5 up to 60 seconds. For further information check out the [cloud documentation](CLOUD.md).
