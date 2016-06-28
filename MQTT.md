# MQTT - IoT Raspberry PI Documentation
On each of the raspberry pi there is a [RabbitMQ Server](http://www.rabbitmq.com) up and running.

## Service
To check out the status, restart or stop the mqtt server just use the service command:
```sudo service rabbitmq-server start|stop|status|restart}```

## Connect
The MQTT Server is listening on the port ```5672```.
There are a examples to recieve data from the sensors in the ```/home/pi/IoT-Hackathon/helper/sensor-mqtt-reciever``` folder.

The default exchange name is ```iot_hackathon``` and you can use the name of the sensor as the routingkey (e.g. "dht22", "tsl2591" or "#" as a wildcard)

A basic python script to recieve message from the RabbitMQ server could be as following:
```
import pika
import sys

def callback(ch, method, properties, body):
    print "Routingkey: {0} Message: {1}".format(method.routing_key, body)

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()

channel.exchange_declare(exchange='iot_hackathon',
                         type='topic')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='iot_hackathon',
                   queue=queue_name,
                   routing_key='#')


channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()
```

## Exchange and Topics/Routing Keys
* Default Exchange: ```iot_hackathon```
* Topics:
  * ```dht22``
  * ```tsl2591``
  * ```l3gd20``
  * ```lsm303```
  * ```mtk3339`` : Note the GPS Sensor isnt by default connected to the raspberrypi
