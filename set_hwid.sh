#!/bin/bash
if [[ $# -ne 8 ]]; 
    then echo "illegal number of parameters: $0 <16 bit> .... <16 bit>  (8 times)"
    exit
fi
sudo python3 ModbusMessage.py -a 0 -c wregs -s 0 -o 8 -d $1 -P $RS485_COMPORT
