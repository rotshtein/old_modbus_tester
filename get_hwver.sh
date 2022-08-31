#!/bin/bash
if [[ $# -ne 1 ]]; 
    then echo "illegal number of parameters: $0 <address> <hw version>"
    exit
fi
./ModbusMessage.py -a $1 -c rreg -s 24  -P $RS485_COMPORT