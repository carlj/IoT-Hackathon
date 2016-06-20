#!/bin/bash

# Install general packages
sudo pip install RPi.GPIO
#sudo pip install picamera
#sudo pip install requests
#sudo pip install pygame
#sudo pip install pygameui

# Install the LSM303 sources
sudo ./LSM303/install-lsm303.sh

# Install the MTK3339 sources
sudo ./MTK3339/install-mtk3339.sh

# Install the DHT22 sources
sudo ./DHT-22/install-dht22.sh

# Install the L3GD20 sources
sudo ./L3GD20/install-l3gd20.sh

# Install the TSL2591 sources
sudo ./TSL2591/install-tsl2591.sh
