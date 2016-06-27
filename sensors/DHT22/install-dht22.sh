#!/bin/bash
cd "$(dirname "$0")"

#git clone https://github.com/adafruit/Adafruit_Python_DHT.git
cd ./source/Adafruit_Python_DHT-master

sudo apt-get update
sudo apt-get install build-essential python-dev python-openssl

sudo python setup.py install
