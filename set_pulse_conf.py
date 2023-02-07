#!/usr/bin/python3
import ModbusMessage
import click

def get_conf(conf:str) -> int:
    data = {'single': 0, 'dual':1, 'ssr':2,'highRate':3}
    if conf not in data:
        return 0
    return data[conf]    


@click.command()
@click.option('--address','-a', type=int, default=250, help='VMA modbus address')
@click.option('--ComPort', '-P', type=str, help='Comm port name')
@click.option('--Baudrate', '-r', type=int, help='Communication baud rate')
@click.option('--Verbose', '-V', is_flag=True, help='Show aditional modbus details')
@click.option('--conf', '-c', type=click.Choice(['single', 'dual', 'ssr', 'highRate']))
def main(address:int, comport:int, baudrate:int, conf:str, verbose):
    params = ['-c', 'wreg', '-s', '76']
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
    
    params.append('-d')
    params.append(str(get_conf(conf)))
    
    ModbusMessage.main(params)

if __name__ == '__main__':
    main()
