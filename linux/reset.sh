#!/bin/bash
if [[ $# -ne 1 ]]; 
    then echo "illegal number of parameters: $0 <address>"
    exit
fi
../ModbusMessage.py -a $1 -c wreg -s 52 -d 1  -P $RS485_COMPORT