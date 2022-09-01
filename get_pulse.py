#!/usr/bin/python3
import ModbusMessage
import click

@click.command()
@click.option('--address','-a', type=int, default=250, help='VMA modbus address')
@click.option('--ComPort', '-P', type=str, help='Comm port name')
@click.option('--Baudrate', '-r', type=int, help='Communication baud rate')
@click.option('--Verbose', '-V', is_flag=True, help='Show aditional modbus details')   
def main(address:int, comport:int, baudrate:int, verbose:bool):
    params = ['-c', 'rregs', '-s', '16', '-o', '2', '-q']
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
    print('[CH1-LSB,CH1-MSB]')
    ret = (ModbusMessage.main(params, standalone_mode=False))
    print (ret)

if __name__ == '__main__':
    main()
