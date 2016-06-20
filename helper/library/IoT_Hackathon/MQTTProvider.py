import DataConsumer
import pika
import sys

class MQTTProvider:

    def __init__(self, host='localhost', mqttIdentifier='test', socket_address='/tmp/uds_socket'):
        self.__host = host
        self.__mqttIdentifier = mqttIdentifier
        self.__socket = socket_address


    def openConnection(self):
        self.__connection = pika.BlockingConnection(pika.ConnectionParameters(host=host))

        self.__channel = connection.channel()

        channel.exchange_declare(exchange='iot_hackathon',
                                 type='topic')

    def start(self):
        DataConsumer.start(self.__socket, self.__mqttCallback)

    def closeConnection(self):
        self.__connection.close()

    def __mqttCallback(self, data):
        self.__channel.basic_publish(exchange='iot_hackathon',
                                    routing_key=self.__mqttIdentifier,
                                    body=data)
        #print(" [x] Sent %r:%r" % (mqttIdentifier, data))

if __name__ == '__main__':

    socket_address = './uds_socket'
    mqttIdentifier = 'test'
    if len(sys.argv) == 3:
        socket_address = sys.argv[1]
        mqttIdentifier = sys.argv[2]

    mqttProvider = MQTTProvider('localhost', mqttIdentifier, socket_address)
    mqttProvider.openConnection()
    mqttProvider.start()
    mqttProvider.closeConnection()
