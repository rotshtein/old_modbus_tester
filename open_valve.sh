#!/bin/bash
if [[ $# -ne 1 ]]; 
    then echo "illegal number of parameters: $0 <address>"
    exit
fi
sudo python3 ModbusMessage.py -a $1 -c wreg -s 24 -d 65283