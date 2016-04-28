import socket
import sys
import time

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

    # Send data
    message = 'This is the message.  It will be repeated.'
    #print >>sys.stderr, 'sending "%s"' % message
    # sock.sendall(message)

    data = " "
    while len(data) > 0:
        data = sock.recv(4096)
        print >>sys.stderr, '{1} received {0}'.format(data, time.time())

    #print >>sys.stderr, 'sending "%s"' % message

#    amount_received = 0
    #amount_expected = len(message)

    #while amount_received < amount_expected:
    #    data = sock.recv(16)
    #    amount_received += len(data)
    #    print >>sys.stderr, 'received "%s"' % data

finally:
    print >>sys.stderr, 'closing socket'
    sock.close()