#!/bin/bash
cd "$(dirname "$0")"

# Install the GPIO dependencies
sudo pip install --yes Adafruit-GPIO

# Go to the right folder
cd ./source/Adafruit-Raspberry-Pi-Python-Code-master
sudo python setup.py install
