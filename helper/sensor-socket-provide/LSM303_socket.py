import Adafruit_LSM303
from IoT_Hackathon import DataProvider
import sys
import time

lsm303 = None

def lsm303read():
    accel, mag = lsm303.read()
    # Grab the X, Y, Z components from the reading and print them out.
    accel_x, accel_y, accel_z = accel
    mag_x, mag_y, mag_z = mag

    dataDictionary = {'sensor' : 'LSM303',
                      'xAcceleration' : accel_x,
                      'yAcceleration' : accel_y,
                      'zAcceleration' : accel_z,
                      'xMagnitude' : mag_x,
                      'yMagnitude' : mag_y,
                      'zMagnitude' : mag_z}

    return dataDictionary

if __name__ == '__main__':

    lsm303 = Adafruit_LSM303.LSM303()

    socket_address = '/tmp/lsm303'

    if len(sys.argv) == 2:
        socket_address = sys.argv[1]

    DataProvider.start(lsm303read, socket_address)
