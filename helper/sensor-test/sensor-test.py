
def testDHT22():
    print "## Start DHT22"

    import Adafruit_DHT
    sensor = Adafruit_DHT.DHT22
    pin = 4

    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

    if humidity is not None and temperature is not None:
        print('DHT22: Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
    else:
        print('DHT22: Failed to get reading. Try again!')

    print "## END DHT22"

def testL3GD20():
    print "## Start DHT22"

    from Adafruit_L3GD20 import L3GD20
    import time

    gyro = L3GD20(L3GD20.L3DS20_RANGE_250DPS)
    readout = gyro.read()

    print "L3GD20: {0}".format(readout)

    print "## END L3GD20"


def testLSM303():
    print "## Start LSM303"

    import time
    import Adafruit_LSM303

    lsm303 = Adafruit_LSM303.LSM303()
    accel, mag = lsm303.read()

    print "LSM303: {0} : {1}".format(accel, mag)

    print "## End LSM303"


def testTSL2591():
    print "## Start TSL2591"

    from TSL2591 import TSL2591
    tsl = TSL2591()

    full, ir = tsl.get_full_luminosity()
    lux = tsl.calculate_lux(full, ir)
    print "TSL2591: lux {0} full {1} ir {2}".format(lux, full, ir)

    print "## End TSL2591"

if __name__ == '__main__':
    testDHT22()
    testL3GD20()
    testLSM303()
    testTSL2591()

