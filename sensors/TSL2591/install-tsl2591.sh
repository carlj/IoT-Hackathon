#!/bin/bash
cd "$(dirname "$0")"

# Install he needed CFFI dependency
sudo apt-get install --yes libffi-dev

# Install the smbus pip project
sudo pip install smbus-cffi

# Install the sources
cd ./source/python-tsl2591-master
sudo python setup.py install
