import socket
import sys
import time

def start(server_address):
    # Create a UDS socket
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
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
            print >>sys.stderr, '{1} received {0}'.format(data, time.time())

    finally:
        print >>sys.stderr, 'closing socket'
        sock.close()

if __name__ == "__main__":

    start('./uds_socket')
