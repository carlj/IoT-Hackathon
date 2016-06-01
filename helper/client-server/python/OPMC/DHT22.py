import Adafruit_DHT
import DataProvider
import sys

def roundFloatData(data):
    return float(format(data, '.2f'))

def dht22Read():
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 4)

    dataDictionary = {'sensor' : 'DHT22'}
    if humidity is not None:
        dataDictionary['humidity'] = roundFloatData(humidity)
    if temperature is not None:
        dataDictionary['temperature'] = roundFloatData(temperature)

    return dataDictionary

if __name__ == '__main__':

    socket_address = './uds_socket'

    if len(sys.argv) == 2:
        socket_address = sys.argv[1]

    DataProvider.start(dht22Read, socket_address)
