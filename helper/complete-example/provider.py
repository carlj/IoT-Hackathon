import SocketServer
import os
import time
import sys
import Adafruit_DHT
import json

class ThreadingSocketServer(SocketServer.ThreadingMixIn, SocketServer.UnixStreamServer):
     # Ctrl-C will cleanly kill all spawned threads
    daemon_threads = True
    allow_reuse_address = True

    def __init__(self, server_address, RequestHandlerClass):
        SocketServer.UnixStreamServer.__init__(self, server_address, RequestHandlerClass)

class DHT22SockerHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        while True:
            start_time = time.time()
            humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 4)
            try:
                if humidity is not None and temperature is not None:
                    data = json.dumps({"sensor" : "dht22", "humidity" : humidity, "temperature" : temperature})
                    self.request.sendall(data)

                    delta_time = time.time() - start_time
                    if delta_time < 2:
                        time.sleep(2 - delta_time)

            except Exception as e:
                print >> sys.stderr, '###\nException: {0} \nFrom Client: {1.request}\n###'.format(e, self)
                break

if __name__ == "__main__":
    server_address = './uds_socket'
    server = ThreadingSocketServer(server_address, DHT22SockerHandler)
    os.chmod(server_address, 0777)

    try:
        print 'Startet Server'
        server.serve_forever()
    except KeyboardInterrupt:
        print 'Need to close Server'
        server.server_close()
        os.remove(server_address)
