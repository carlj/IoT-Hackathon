import SocketServer
import os
import time
import sys

class ThreadingSocketServer(SocketServer.ThreadingMixIn, SocketServer.UnixStreamServer):
     # Ctrl-C will cleanly kill all spawned threads
    daemon_threads = True
    # much faster rebinding
    allow_reuse_address = True

    def __init__(self, server_address, RequestHandlerClass):
        SocketServer.UnixStreamServer.__init__(self, server_address, RequestHandlerClass)

class MySocketHandler(SocketServer.BaseRequestHandler):

    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        # self.data = self.request.recv(4096).strip()
        # print self.data
        # print self.client_address[0]

        # just send back the same data, but upper-cased
        while True:
            try:
                self.request.sendall("Hello World")
                print '{1}: Sended to client {0.request}'.format(self, time.time())
                time.sleep(0.1)
            except Exception as e:
                print >> sys.stderr, '###\nException: {0} \nFrom Client: {1.request}\n###'.format(e, self)
                break

if __name__ == "__main__":
    server_address = './uds_socket'
    server = ThreadingSocketServer(server_address, MySocketHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C

    try:
        print 'Startet Server'
        server.serve_forever()
    except KeyboardInterrupt:
        print 'Need to close Server'
        server.server_close()
        os.remove(server_address)
