#!/bin/bash

# Install the GPIO dependencies
sudo pip install Adafruit-GPIO

# Go to the right folder
cd ./source/Adafruit-Raspberry-Pi-Python-Code-master
sudo python install setup.py install
