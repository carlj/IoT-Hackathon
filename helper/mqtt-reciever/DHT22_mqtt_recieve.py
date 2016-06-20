from IoT_Hackthon import MQTTReciever

def callback(key, body):
    print 'Key: {0} body {1}'.format(key, body)

if __name__ == '__main__':

    recieve = MQTTReciever('localhost', 'dht22', callback)
    revieve.openConnection()
