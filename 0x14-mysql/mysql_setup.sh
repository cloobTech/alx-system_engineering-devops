#!/usr/bin/env bash

# Update package index and install MySQL server package
sudo apt-get update
sudo apt-get install mysql-server-5.7

# Check MySQL service status
sudo systemctl status mysql

# Start MySQL service if not already running
sudo systemctl start mysql

# Enable MySQL service on boot
sudo systemctl enable mysql

# Check MySQL service status again
sudo systemctl status mysql
