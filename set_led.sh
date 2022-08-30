#!/bin/bash
if [[ $# -ne 2 ]]; 
    then echo "illegal number of parameters: $0 <address> <hw version>"
    exit
fi
sudo python3 ModbusMessage.py -a $1 -c wreg -s 28 -d $2