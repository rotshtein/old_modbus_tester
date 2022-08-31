#!/bin/bash
if [[ $# -ne 2 ]]; 
    then echo "illegal number of parameters: $0 <16 bit> .... <16 bit>  (8 times)"
    exit
fi
../ModbusMessage.py -a 0 -c wregs -s 0 -o 8 -D $1 -P $RS485_COMPORT
