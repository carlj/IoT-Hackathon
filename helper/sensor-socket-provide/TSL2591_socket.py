from TSL2591 import TSL2591
from IoT_Hackathon import DataProvider
import sys
import time

tsl = None

def tsl2591read():

    global tsl
    full, ir = tsl.get_full_luminosity()  # read raw values (full spectrum and ir spectrum)
    lux = tsl.calculate_lux(full, ir)  # convert raw values to lux

    dataDictionary = {'sensor' : 'TSL2591',
                      'lux' : lux,
                      'fullspectrum' : full,
                      'irspectrum' : ir}

    return dataDictionary

if __name__ == '__main__':

    tsl = TSL2591()

    socket_address = '/tmp/tsl2591'

    if len(sys.argv) == 2:
        socket_address = sys.argv[1]

    DataProvider.start(tsl2591read, socket_address)
