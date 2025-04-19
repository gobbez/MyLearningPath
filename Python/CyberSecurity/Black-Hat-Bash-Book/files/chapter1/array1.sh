#!/bin/bash

# Create array
IP_ADDRESS=(192.168.1.1 192.168.1.3)

# Show all
echo ${IP_ADDRESS[*]}

# Show first
echo ${IP_ADDRESS[0]}
