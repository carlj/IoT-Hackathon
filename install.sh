#!/bin/bash
cd "$(dirname "$0")"

# Install I2C needed packages
sudo apt-get update
sudo apt-get install --yes python-smbus
sudo apt-get install --yes i2c-tools

# Install Python GPIO support
sudo apt-get install --yes python-dev
sudo apt-get install --yes python-rpi.gpio

# Install RabbitMQ
echo 'deb http://www.rabbitmq.com/debian/ testing main' | sudo tee /etc/apt/sources.list.d/rabbitmq.list
wget -O- https://www.rabbitmq.com/rabbitmq-release-signing-key.asc | sudo apt-key add -
sudo apt-get install --yes rabbitmq-server

sudo cp ./helper/rabbitmq/rabbitmq.config /etc/rabbitmq/rabbitmq.config

sudo rabbitmqctl set_policy TTL ".*" '{"message-ttl":5000}' --apply-to queues

# Install the Sensor Libraries
sudo ./sensors/install-sensors.sh

# Install the Helper Library
sudo ./helper/library/install-library.sh

# Install the Services
sudo ./helper/services/install-services.sh

# Reboot
echo "Please reboot with: 'sudo shutdown -r now'"
