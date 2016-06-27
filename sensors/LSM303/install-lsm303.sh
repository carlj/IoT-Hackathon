#!/bin/bash
cd "$(dirname "$0")"

sudo apt-get install git build-essential python-dev

#git clone https://github.com/adafruit/Adafruit_Python_LSM303.git
cd ./source/Adafruit_Python_LSM303-master
sudo python setup.py install
