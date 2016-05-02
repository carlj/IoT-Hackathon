#!/usr/bin/env python
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='192.168.188.24'))
channel = connection.channel()

channel.exchange_declare(exchange='iot_logs',
                         type='topic')

channel.basic_publish(exchange='iot_logs',
                      routing_key="test",
                      body="TEst")
print(" [x] Sent %r:%r" % ("test", message))
connection.close()
