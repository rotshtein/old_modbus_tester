#!/usr/bin/python3
import ModbusMessage
import click

@click.command()
@click.option('--address','-a', type=int, default=1, help='VMA modbus address')
@click.option('--color','-d', type=int, default=6, help='led_color (6-for green blink, 0-off')
@click.option('--ComPort', '-P', type=str, default = '/dev/ttyS0', help='Comm port name')
@click.option('--Baudrate', '-r', type=int, default = 38400, help='Communication baud rate')
@click.option('--Verbose', '-V', is_flag=True, help='Show aditional modbus details')   
def main(address:int, color:int, comport:int, baudrate:int, verbose:bool):
    params = ['-a', address, '-c', 'wreg', '-s', '28', '-d', color,'-P', comport, '-r', baudrate]
    if verbose:
        params.append('-V')
    ModbusMessage.main(params)

if __name__ == '__main__':
    main()
