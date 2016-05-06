import Adafruit_DHT
import data_provider

def newData():
    return "1"

if __name__ == "__main__":

    poller = data_provider.DataPoller(newData)
    poller.start()

    server_address = './uds_socket'
    server = data_provider.ThreadingSocketServer(server_address, data_provider.MySocketHandler)

    try:
        print 'Startet Server'
        server.serve_forever()
    except KeyboardInterrupt:
        print 'Need to close Server'
        server.server_close()
        os.remove(server_address)
        poller.running = False
        poller.join()
