#!/bin/bash

# Install I2C needed packages
sudo apt-get update
sudo apt-get install python-smbus
sudo apt-get install i2c-tools

# Install Python GPIO support
sudo apt-get install python-dev
sudo apt-get install python-rpi.gpio

# Install RabbitMQ
echo 'deb http://www.rabbitmq.com/debian/ testing main' | sudo tee /etc/apt/sources.list.d/rabbitmq.list
wget -O- https://www.rabbitmq.com/rabbitmq-release-signing-key.asc | sudo apt-key add -
sudo apt-get install rabbitmq-server

sudo cp ./helper/rabbitmq/rabbitmq.config /etc/rabbitmq/rabbitmq.config 

# Install the Sensor Libraries
sudo ./sensors/install.sh

# Install the Helper Library
sudo ./helper/install.sh

# Reboot
echo "Please reboot with: 'sudo shutdown -r now'"
