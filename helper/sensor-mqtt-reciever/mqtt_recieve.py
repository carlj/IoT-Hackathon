from IoT_Hackathon import MQTTReciever
import sys

def callback(key, body):
    print 'Key: {0} body {1}'.format(key, body)

if __name__ == '__main__':

    topic = 'dht22'
    host = 'localhost'
    if len(sys.argv) == 1:
        print "You need to provide at least the sensor name (dht22, lsm303, tsl2591, mtk3399 or l3gd20) as a parameter e.g. (sudo python mqtt_recieve.py 'dht22')"
        exit(-1)

    if len(sys.argv) >= 2:
        topic = sys.argv[1]

    if len(sys.argv) >= 3:
        host = sys.argv[2]

    recieve = MQTTReciever(host, topic, callback)
    recieve.openConnection()
