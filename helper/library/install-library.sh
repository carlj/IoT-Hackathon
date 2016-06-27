#!/bin/bash
cd "$(dirname "$0")"

## Install Iot-Hackathon PIP package
sudo pip install pika

sudo python setup.py install
