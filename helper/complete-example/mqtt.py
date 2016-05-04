import socket
import sys
import time
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='iot_logs', type='topic')

# Create a UDS socket
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = './uds_socket'
print >>sys.stderr, 'connecting to %s' % server_address
try:
    sock.connect(server_address)
except socket.error, msg:
    print >>sys.stderr, 'Error: %s' % msg
    sys.exit(1)

try:
    data = " "
    while len(data) > 0:
        data = sock.recv(4096)
        channel.basic_publish(exchange='iot_logs',
                              routing_key="iot.dht22",
                              body=data)
        print "{1} received {0}".format(data, time.time())

finally:
    print >>sys.stderr, 'closing socket'
    sock.close()



connection.close()