import ModbusMessage
import sys, click

#@click.command()
#@click.option('--address','-a', type=int, default=1, help='VMA modbus address')
def main():
    ModbusMessage.main ('-a 1')

if __name__ == '__main__':
    main()
