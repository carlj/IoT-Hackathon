#!/usr/bin/env python
import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='192.168.188.24'))
channel = connection.channel()

channel.queue_declare(queue='hello', durable=False,
arguments={
  'x-message-ttl' : 1000,
  'x-max-length': 100}
)

def callback(ch, method, properties, body):
    print("{1} [x] Received {0}".format(body, time.time()))

channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
