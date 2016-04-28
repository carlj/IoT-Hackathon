#!/usr/bin/env python
import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello', durable=False,
arguments={
  'x-message-ttl' : 1000,
  'x-max-length': 100}
)



while True:
    try:
        channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
        print(" [x] Sent 'Hello World!'")


    except Exception as e:
        print("{0}".format(e))
        connection.close()
