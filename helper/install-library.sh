#!/bin/bash
cd "$(dirname "$0")"

## Install Iot-Hackathon PIP package
sudo pip install pika

cd ./library/IoT_Hackathon
sudo python setup.py install
