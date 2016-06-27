from IoT_Hackathon import MQTTProvider
import sys

if __name__ == '__main__':

    host = 'localhost'
    topic = 'dht22'
    socket = '/tmp/dht22'
    if len(sys.argv) == 4:
        host = sys.argv[1]
        topic = sys.argv[2]
        socket = sys.argv[3]
    else:
        print "you need to provide the host, topic and socket (e.g. 'sudo python mqtt_provide.py localhost dht22 /tmp/dht22')"
    
    mqttProvider = MQTTProvider(host, topic, socket)
    mqttProvider.openConnection()
    mqttProvider.start()
    mqttProvider.closeConnection()
