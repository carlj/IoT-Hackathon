import SocketServer
import os
import time
import sys
import threading

sessionData = None #seting the global variable


class DataPoller(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    global sessionData 
    sessionData = 0

    self.current_value = None
    self.running = True #setting the thread running to true

  def run(self):
    global sessionData
    while self.running:
        sessionData = time.time()
        time.sleep(1.)


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
        global sessionData
        previousData = sessionData
        while True:
            try:
                if previousData != sessionData:
                    self.request.sendall('{0}'.format(sessionData))
                    previousData = sessionData
                    print '{1}: Sended to client {0.request}. {1}'.format(self, sessionData)
                time.sleep(0.1)
            except Exception as e:
                print >> sys.stderr, '###\nException: {0} \nFrom Client: {1.request}\n###'.format(e, self)
                break

if __name__ == "__main__":

    poller = DataPoller()
    poller.start()

    server_address = './uds_socket'
    server = ThreadingSocketServer(server_address, MySocketHandler)

    try:
        print 'Startet Server'
        server.serve_forever()
    except KeyboardInterrupt:
        print 'Need to close Server'
        server.server_close()
        os.remove(server_address)

        poller.running = False
        poller.join()
