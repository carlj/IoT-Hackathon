# IoT Raspberry PI Documentation

## Installation

You can find the installation documentation [here](INSTALLATION.md)

## Connect
There are three different ways to connect to the Raspberry PI:

**Graphic**: You can directly connect the Raspberry Pi to a HDMI display, Keyboard and Mouse.

**SSH**: On every raspberry pi there is a ssh server running. To connect to the rasberrypi just try to run the command ```ssh pi@IP-FOR-YOU-RASPBERRY``` or ```ssh pi@NAME-OF-YOUR-RASPBERRY``` e.g. ```ssh pi@raspberrypi9```. The user is ```pi``` and the password is ```raspberry```.

**Console Cable**:
If you want to connect via a Console Cable you need to install the following driver for the **PL2303** USB to TTL Chipset on you local machine: http://www.prolific.com.tw/US/ShowProduct.aspx?pcid=41&showlevel=0041-0041.


You also need to connect the black, green and white cable with the raspberry as shown in the picture:
![TTL Connection](https://cdn-learn.adafruit.com/assets/assets/000/003/118/medium800/learn_raspberry_pi_overview.jpg?1396791615)

* On linux and Mac OS X you can run the command ```screen /dev/ttyUSBSerial 115200``` to connect to the Raspberry Pi.
* Within Windows you need to download [Putty](http://www.putty.org). You can find the com port by looking in the Ports section of the Windows Device Manager.

For further information you can check out the tutorial from Adafruit: https://learn.adafruit.com/adafruits-raspberry-pi-lesson-5-using-a-console-cable/overview

If everything is up and running you can check out the python script for the sensors. 

## Sensor's
With the current setup we provided a bunch of sensor's:
* [DHT22]( https://www.adafruit.com/products/385): The DHT22 is a basic, low-cost **digital temperature** and **humidity sensor**. It uses a capacitive humidity sensor and a thermistor to measure the surrounding air, and spits out a digital signal on the data pin (no analog input pins needed). Its fairly simple to use, but requires careful timing to grab data. The only real **downside of this sensor is you can only get new data from it once every 2 seconds**, so when using our library, sensor readings can be up to 2 seconds old.

* [MTK3339](https://www.adafruit.com/products/746): The MKT3339 is a high-quality **GPS module** that can track up to 22 satellites on 66 channels, has an excellent high-sensitivity receiver (-165 dB tracking!), and a built in antenna. It can do up to 10 location updates a second for high speed, high sensitivity logging or tracking. Power usage is incredibly low, only 20 mA during navigation.  
**Note: The GPS module isnt connected by default to the raspberry pi. To connect the GPS module read the instruction in the [GPS Installation Docu](sensors/MTK3339/README.md)**

* [TSL2561](https://www.adafruit.com/products/439): The TSL2561 **luminosity sensor** is an advanced digital light sensor, ideal for use in a wide range of light situations. Compared to low cost CdS cells, this sensor is more precise, allowing for exact lux calculations and can be configured for different gain/timing ranges to detect light ranges from up to 0.1 - 40,000+ Lux on the fly. The best part of this sensor is that it contains both **infrared and full spectrum diodes**!

* [L3GD20 / LSM303](https://www.adafruit.com/products/1714): This inertial-measurement-unit combines 2 of the best quality sensors available on the market to give you 9 axes of data: **3 axes of accelerometer data, 3 axes gyroscopic, and 3 axes magnetic (compass)**.

### Using the Sensor's
There are a few different way's to interact with the sensors. For further Information check out the [Service Docu](SERVICES.md)
