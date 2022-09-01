#!/usr/bin/python3
import ModbusMessage
import click
from typing import List

def convert_to_data_list(id:str) -> List:
    return [0,0,0,int(id[0:2]), int(id[2:4]), int(id[4:6]), int(id[6:8]), int(id[8:])]


@click.command() 
@click.option('--hwid','-d', type=str, required=True, help='VMA modbus address')
@click.option('--ComPort', '-P', type=str, help='Comm port name')
@click.option('--Baudrate', '-r', type=int, help='Communication baud rate')
@click.option('--Verbose', '-V', is_flag=True, help='Show aditional modbus details')   
def main(hwid:str, comport:int, baudrate:int, verbose:bool):
    data_list = convert_to_data_list(hwid)
    params = ['-a', 0, '-c', 'wregs', '-s', '0', '-o', '8']
    for data_param in data_list:
        params.extend(['-d', data_param])
    
    if comport is not None:
        params.append('-P') 
        params.append(comport)
    if baudrate is not None:
        params.append('-r')
        params.append(str(baudrate))
    if verbose:
        params.append('-V')
    ret = ModbusMessage.main(params)
    print (ret)

if __name__ == '__main__':
    main()
