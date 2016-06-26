#!/bin/bash

## Install Iot-Hackathon PIP package
sudo pip install pika

cd ./library/iot-hackathon
sudo python setup.py install

## Install services
cd ./services
sudo ./install.sh
