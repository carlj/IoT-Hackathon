from Adafruit_L3GD20 import L3GD20
from IoT_Hackathon import DataProvider
import sys
import time

def getAvgDrift(gyro):

    gyroXAngle = gyroYAngle = gyroZAngle = 0

    sampleCnt = 500

    for i in range(0, sampleCnt):
        readout = gyro.read()
        gyroXAngle += readout[0]
        gyroYAngle += readout[1]
        gyroZAngle += readout[2]
        time.sleep(0.02)

    return (
        gyroXAngle / sampleCnt,
        gyroYAngle / sampleCnt,
        gyroZAngle / sampleCnt
    )

def roundFloatData(data):
    return float(format(data, '.2f'))


avgDrift = None
gyro = None
lastTime = None

def l3gd20read():

    global gyro
    readout = gyro.read()

    global lastTime
    currentTime = time.time() * 1000
    timeDiff = currentTime - lastTime
    lastTime = currentTime

    global avgDrift
    gyroXAngle = (readout[0] - avgDrift[0]) * gyro.GAIN #* (timeDiff / 1000)
    gyroYAngle = (readout[1] - avgDrift[1]) * gyro.GAIN #* (timeDiff / 1000)
    gyroZAngle = (readout[2] - avgDrift[2]) * gyro.GAIN #* (timeDiff / 1000)

    dataDictionary = {'sensor' : 'L3GD20',
                      'xAngle' : gyroXAngle,
                      'yAngle' : gyroYAngle,
                      'zAngle' : gyroZAngle}

    return dataDictionary

if __name__ == '__main__':

    global gyro
    gyro = L3GD20(L3GD20.L3DS20_RANGE_250DPS)

    global avgDrift
    avgDrift = getAvgDrift(gyro)

    global lastTime
    lastTime = time.time() * 1000

    socket_address = '/tmp/l3gd20'

    if len(sys.argv) == 2:
        socket_address = sys.argv[1]

    DataProvider.start(l3gd20read, socket_address)
