#!/bin/bash
cd "$(dirname "$0")"

# Install DHT22 Service
sudo cp dht22.service /etc/systemd/system/dht22.service
sudo cp dht22-mqtt.service  /etc/systemd/system/dht22-mqtt.service

sudo systemctl enable dht22.service
sudo systemctl enable dht22-mqtt.service

# Install L3GD20 Service
sudo cp l3gd20.service /etc/systemd/system/l3gd20.service
sudo cp l3gd20-mqtt.service  /etc/systemd/system/l3gd20-mqtt.service

sudo systemctl enable l3gd20.service
sudo systemctl enable l3gd20-mqtt.service

# Install LSM303 Service
sudo cp lsm303.service /etc/systemd/system/lsm303.service
sudo cp lsm303.service  /etc/systemd/system/lsm303-mqtt.service

sudo systemctl enable lsm303.service
sudo systemctl enable lsm303-mqtt.service

# Install MTK3339 Service
sudo cp mtk3339.service /etc/systemd/system/mtk3339.service
sudo cp mtk3339-mqtt.service  /etc/systemd/system/mtk3339-mqtt.service

#sudo systemctl enable mtk3339.service
#sudo systemctl enable mtk3339-mqtt.service

# Install TSL2591 Service
sudo cp tsl2591.service /etc/systemd/system/tsl2591.service
sudo cp tsl2591-mqtt.service  /etc/systemd/system/tsl2591-mqtt.service

sudo systemctl enable tsl2591.service
sudo systemctl enable tsl2591-mqtt.service
