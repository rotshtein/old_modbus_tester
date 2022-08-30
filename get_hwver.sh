#!/bin/bash
if [[ $# -ne 1 ]]; 
    then echo "illegal number of parameters: $0 <address> <hw version>"
    exit
fi
sudo python3 ModbusMessage.py -a $1 -c rreg -s 24 