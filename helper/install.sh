#!/bin/bash
cd "$(dirname "$0")"

## Install Iot-Hackathon PIP package
sudo pip install pika

cd ./library/iot-hackathon
sudo python setup.py install
