import pika
import sys

class MQTTReciever:

    def __init__(self, host='localhost', routing_key='#', callback=None):
        self.__host = host
        self.__routingKey = routing_key
        self.__callback = callback

    def __internalCallback(ch, method, properties, body):
        if self.__callback:
            self.__callback(method.routing_key, body)

    def openConnection(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters(
                host=self.__host))
        channel = connection.channel()

        channel.exchange_declare(exchange='iot_hackathon',
                                 type='topic')

        result = channel.queue_declare(exclusive=True)
        queue_name = result.method.queue

        channel.queue_bind(exchange='iot_hackathon',
                               queue=queue_name,
                               routing_key=self.__routingKey)


        channel.basic_consume(self.__internalCallback,
                              queue=queue_name,
                              no_ack=True)

        channel.start_consuming()

if __name__ == '__main__':

    def callback(key, body):
        print 'Key: {0} body {1}'.format(key, body)

    recieve = MQTTReciever('localhost', '#', callback)
    revieve.openConnection()
