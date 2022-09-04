#!/usr/bin/python3
import ModbusMessage
import click

@click.command()
@click.option('--address','-a', type=int, default=250, help='VMA modbus address')
@click.option('--ComPort', '-P', type=str, help='Comm port name')
@click.option('--Baudrate', '-r', type=int, help='Communication baud rate')
@click.option('--Verbose', '-V', is_flag=True, help='Show aditional modbus details')   
def main(address:int, comport:int, baudrate:int, verbose:bool):
    params = ['-c', 'rregs', '-s', '0', '-o', '8', '-q']
    if address is not None:
        params.append('-a')
        params.append(str(address))
    if comport is not None:
        params.append('-P') 
        params.append(comport)
    if baudrate is not None:
        params.append('-r')
        params.append(str(baudrate))
    if verbose:
        params.append('-V')
    ret = ModbusMessage.main(params, standalone_mode=False)
    print('=================================================================================================')
    print('|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |')
    print('|  PCB +  PCBA    |P CH1|P CH2| SSR | HRP |ADC#1|ADC#2| VLV |        Spare                      |')
    print('================================================================================================ ')
    if isinstance(ret, list) and len(ret) == 8:
        pass    
    print (ret)

if __name__ == '__main__':
    main()