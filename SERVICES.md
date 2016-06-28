# Sensors - IoT Raspberry PI Documentation

## Usage

***Locally***:
* **Do it by yourself**: If you are happy and a crazy nerd you can do everything by yourself. The sensors are already connected to the Raspberry PI's GPIO or i2c ports and feel free to develop in any language you would like.
* **Example Python Scripts**: In the ```/home/pi/IoT-Hackathon/sensors``` directory are folders for every sensor. You can check out the specific example folder (e.g ```/home/pi/IoT-Hackathon/sensors/dht22/example```) for a python script to work with the sensor data and get an idea how to interact with the data itself.
* **Local Server**: For each of the sensor there is a local [unix domain socket server](https://en.wikipedia.org/wiki/Unix_domain_socket) running. You can connect **only locally** to the server by connecting to the socket for the sensor (e.g ```/tmp/dht22```). There is also a client example for the sensors in the ```/home/pi/IoT-Hackathon/helper/sensor-socket-recieve``` directory.

**Note**: For the Remote solution, mentioned below, we are also using the local unix domain socket server. The advantage of this behaviour is that you dont need that start the scripts for every sensor by your self.

***Remote:***
* **MQTT**: If you want to request the sensor data from a remote device directly from the Raspberry PI there is a [RabbitMQ](http://www.rabbitmq.com) server that supports [amqp](https://en.wikipedia.org/wiki/Advanced_Message_Queuing_Protocol) up and running. With this service you have the ability to get real time data from the sensors without develop something on the raspberry itself. For further Information check out the [MQTT Documentation](mqtt.md)

## Scripts

For each of the sensors there are already the ```socker``` and the ```mqtt```scripts implemented. The sources are located in the ```/home/pi/IoT-Hackathon/helper``` folder.


* **library**: This is the IoT-Hackathon Python Library that is used in all of the following examples. You dont need to touch anything in there.
* **rabbitmq**: The rabbitmq folder for the configuration files. You also dont need to touch anything in there.
* **sensor-socket-provide**: There are the python scripts to read data from the sensor and publish the data to a ```local socket``` in the ```/tmp/``` folder
* **sensor-socket-recieve**: Here are the scripts to recieve data from the ```local socket```
* **sensor-mqtt-provide**: In this folder are the scripts located to publish the sensor data from the local socket to the ```mqtt server```
* **sensor-mqtt-reciever**: Here are the script to recieve data from the ```mqtt server```
* **sensor-test**: Included is just a test script for checking if all of the sensors are working correctly.
* **services**: Here are the .service files located for the socket and mqtt scripts. You dont need to touch anything here

## Services
As mentiod above there are services for each sensor to publish data to the ```local socket``` or the ```mqtt server```.

To start the ```local socket``` services for the ```DHT22``` just run the following command:
```
sudo systemctl start dht22 #Starts the local socket service for the DHT22 sensor
```
You can get the status of the services by typing:
```
sudo systemctl status dht22
```
To stop a running services just fire the command:
```
sudo systemctl stop dht22
```
There are local socket services for all of the sensors with the name: dht22, l3gd20, lsm303, mtk3339, tsl2591.
The mqtt services are named as the following: dht22-mqtt, l3gd20-mqtt, lsm303-mqtt, mtk3339-mqtt, tsl2591-mqtt. Note that the ```mqtt services``` will start the related ```socket services``` by there self.
