import Adafruit_DHT
import data_provider
import os

def newData():
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 4)

    dataDictionary = {'sensor' : 'dht22'}
    if humidity is not None:
        dataDictionary['humidity'] = float(format(humidity, '.2f'))
    if temperature is not None:
        dataDictionary['temperature'] = float(format(temperature, '.2f'))

    return dataDictionary

if __name__ == "__main__":

    data_provider.start(newData, './uds_socket')
