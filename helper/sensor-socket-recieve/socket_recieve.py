from IoT_Hackathon import DataConsumer
import sys
import time

def printCallback(data):
    print '{1} received {0}'.format(data, time.time())

if __name__ == '__main__':

    socket = '/tmp/dht22'
    if len(sys.argv) >= 2:
        socket = sys.argv[1]
    else:
        print "You need to provide the sensor socket (/tmp/dht22, /tmp/lsm303, /tmp/tsl2591, /tmp/mtk3399 or /tmp/l3gd20) as a parameter e.g. (sudo python socket_recieve.py '/tmp/dht22')"
        exit(-1)


    DataConsumer.start(socket, printCallback)
