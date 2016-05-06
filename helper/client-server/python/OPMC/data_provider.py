import SocketServer
import os
import time
import sys
import threading
import Queue

queueList = []

class DataPoller(threading.Thread):
  def __init__(self, dataFunction):
    threading.Thread.__init__(self)
    self.dataFunction = dataFunction
    self.running = True #setting the thread running to true


  def run(self):
    global queueList
    while self.running:
        newData = self.dataFunction()
        for q in queueList:
            q.put(newData)
        time.sleep(1.)


class ThreadingSocketServer(SocketServer.ThreadingMixIn, SocketServer.UnixStreamServer):
     # Ctrl-C will cleanly kill all spawned threads
    daemon_threads = True
    # much faster rebinding
    allow_reuse_address = True

    def __init__(self, server_address, RequestHandlerClass):
        SocketServer.UnixStreamServer.__init__(self, server_address, RequestHandlerClass)

class MySocketHandler(SocketServer.BaseRequestHandler):

    def finish(self):
        global queueList
        queueList.remove(self.queue)

    def handle(self):
        global queueList
        q = Queue.Queue()
        queueList.append(q)
        self.queue = q

        while True:
            try:
                data = self.queue.get()
                self.request.sendall('{0}'.format(data))
                print '{1}: Sended to client {0.request}. {1}'.format(self, data)
            except Exception as e:
                print >> sys.stderr, '###\nException: {0} \nFrom Client: {1.request}\n###'.format(e, self)
                break

def newData():
    return time.time()

if __name__ == "__main__":

    poller = DataPoller(newData)
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
