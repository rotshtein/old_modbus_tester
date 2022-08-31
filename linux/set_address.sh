#!/bin/bash

if [[ $# -ne 1 ]]; 
    then echo "illegal number of parameters: set_address.sh <address>"
    exit
fi
../ModbusMessage.py -a 0 -c wreg -s 38 -d %1  -P $RS485_COMPORT -V