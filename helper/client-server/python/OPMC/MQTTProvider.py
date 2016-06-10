import DataConsumer
import pika
import sys

mqttIdentifier = None
channel = None

def openConnection(host):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=host))

    global channel
    channel = connection.channel()

    channel.exchange_declare(exchange='iot_hackathon',
                             type='topic')

    return connection

def closeConnection(connection):
    connection.close()

def mqttCallback(data):
    global channel
    global mqttIdentifier
    channel.basic_publish(exchange='iot_hackathon',
                          routing_key=mqttIdentifier,
                          body=data)
    print(" [x] Sent %r:%r" % (mqttIdentifier, data))

if __name__ == '__main__':

    socket_address = './uds_socket'

    global mqttIdentifier
    mqttIdentifier = 'time'
    if len(sys.argv) == 3:
        socket_address = sys.argv[1]

        mqttIdentifier = sys.argv[2]

    connection = openConnection('localhost')
    DataConsumer.start(socket_address, mqttCallback)
    closeConnection(connection)
