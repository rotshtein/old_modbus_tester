#!/bin/bash
if [[ $# -ne 8 ]]; 
    then echo "illegal number of parameters: $0 <16 bit> .... <16 bit>  (8 times)"
    exit
fi
sudo python3 ModbusMessage.py -a 0 -c wregs -s 0 -o 8 -d $1 -d $2 -d $3 -d $4 -d $5 -d $6 -d $7 -d $8
