from IoT_Hackathon import MQTTProvider

if __name__ == '__main__':

    mqttProvider = MQTTProvider('localhost', 'dht22', '/tmp/dht22')
    mqttProvider.openConnection()
    mqttProvider.start()
    mqttProvider.closeConnection()
