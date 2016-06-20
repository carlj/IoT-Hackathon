#!/bin/bash

# Expand the file system
sudo raspi-config --expand-rootfs

# Install pygame
sudo apt-get update
sudo apt-get build-dep python-pygame
sudo apt-get install python-dev

# Reboot
sudo shutdown -r now
