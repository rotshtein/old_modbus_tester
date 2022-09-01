#!/bin/bash

#if [[ $# -ne 1 ]]; 
#    then echo "illegal number of parameters: $0 <serial>"
#    exit
#fi
echo 'set hw ver'

#./set_hwver.py -d  0x 0020 0101 0101 0000 0100 0000 0000 0000
# PCB 3 | PCBA 3 | Pulse#CH2 | Pulse#CH1 | High rate pulse |  ADC#CH1 | SSR | VLV | ADC#CH2 |      
# =================================================================================================  
# |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
# |  PCB +  PCBA    |P CH1|P CH2| SSR | HRP |ADC#1|ADC#2| VLV |        Spare                      |
#  ================================================================================================ 
./ModbusMessage.py -a 0 -s 54 -c wregs -o 8 -d 32 -d 257 -d 257 -d 0 -d 1 -d 0 -d 0 -d 0

echo 'set address to 250'
./set_address.py

echo 'get hw-ver'
./get_hwver.py

echo 'get serial number'
./get_hwid.py

echo 'close'
./close_valve.py

echo 'wait 10 sec'
sleep 10

echo 'valve state'
./get_valve.py

echo 'open'
./open_valve.py

echo 'wait 10 sec'
sleep 10

echo 'valve state'
./get_valve.py

echo 'pulse'
./get_pulse.py

echo wait 2 sec
sleep 2

echo 'pulse'
./get_pulse.py

echo 'set address to 0 - unpair'
./unpair.py

#echo 'restart the VMA in paring mode'
#read -p 'press any key....'

#echo 'set serial number'
#./ModbusMessage.py -a 0 -s 0 -c wregs -o 8 -D $1



