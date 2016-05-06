import SocketServer
import os
import time
import sys
import threading
import Queue
import json

queueList = []

class DataPoller(threading.Thread):
  def __init__(self, dataFunction):
    threading.Thread.__init__(self)
    self.dataFunction = dataFunction
    self.running = True #setting the thread running to true

  def run(self):
    global queueList
    while self.running:
        if len(queueList) <= 0:
            time.sleep(0.1)
            continue
        newData = self.dataFunction()
        for q in queueList:
            q.put(newData)


class ThreadingSocketServer(SocketServer.ThreadingMixIn, SocketServer.UnixStreamServer):
    daemon_threads = True
    allow_reuse_address = True

class ConsumerHandler(SocketServer.BaseRequestHandler):

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
                jsonData = json.dumps(data)
                self.request.sendall(jsonData)
                print '{1}: Sended to client {0.request}. {1}'.format(self, data)
            except Exception as e:
                print >> sys.stderr, '###\nException: {0} \nFrom Client: {1.request}\n###'.format(e, self)
                break

def newData():
    return time.time()

def start(dataFunction, server_address):
    if dataFunction == None or len(server_address) <= 0:
        print 'Cannot start server'
        return

    poller = DataPoller(dataFunction)
    poller.start()

    server = ThreadingSocketServer(server_address, ConsumerHandler)
    os.chmod(server_address, 0777)

    try:
        print 'Started Server'
        server.serve_forever()
    except KeyboardInterrupt:
        print 'Close Server'
        server.server_close()
        os.remove(server_address)
        poller.running = False
        poller.join()

if __name__ == "__main__":
    start(newData, './uds_socket')
