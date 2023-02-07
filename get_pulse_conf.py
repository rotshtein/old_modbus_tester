#!/usr/bin/python3
import ModbusMessage
import click

def get_conf(conf:int) -> str:
    data = {0:'single', 1: 'dual',2: 'ssr',3: 'highRate'}
    if conf not in data:
        return 'unknown'
    return data[conf]

@click.command()
@click.option('--address','-a', type=int, default=250, help='VMA modbus address')
@click.option('--ComPort', '-P', type=str, help='Comm port name')
@click.option('--Baudrate', '-r', type=int, help='Communication baud rate')
@click.option('--Verbose', '-V', is_flag=True, help='Show aditional modbus details')   
def main(address:int, comport:int, baudrate:int, verbose:bool):
    params = ['-c', 'rreg', '-s', '76', '-o', '1', '-q']
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
    
    ret = (ModbusMessage.main(params, standalone_mode=False))
    if ret is not None:
        print (get_conf(ret))

if __name__ == '__main__':
    main()
