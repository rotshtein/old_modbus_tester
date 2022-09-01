#!/usr/bin/python3
from typing import List
from enum import IntEnum
import minimalmodbus
import click
import sys, os


class  Action(IntEnum):
    READ_BIT = 1,
    WRITE_BIT = 2,
    READ_BITS = 3,
    WRITE_BITS = 4,
    READ_REGISTER = 5,
    WRITE_REGISTER = 6,
    READ_LONG = 7,
    WRITE_LONG = 8,
    READ_FLOAT = 9,
    WRITE_FLOAT = 10,
    READ_STRING = 11,
    WRITE_STRING = 12,
    READ_REGISTERS = 13,
    WRITE_REGISTERS = 14
    

class ModbusMessage:
    MAX_DATA = 256-10-2  # 256 - header & CRC - chunk number
    
    def __init__(self, address:int, Debug:bool = False, ComPort:str='/dev/ttyS0', baud_rate:int = 38400) -> None:
        self.address = address
        self.ComPort = ComPort
        self.modbus_instrument = minimalmodbus.Instrument(port=ComPort, slaveaddress=0, close_port_after_each_call=True)
        self.modbus_instrument.MODE_RTU= 'rtu'
        self.modbus_instrument.serial.baudrate = baud_rate
        self.modbus_instrument.serial.parity = 'N'
        self.modbus_instrument.serial.stopbits = 1
        self.modbus_instrument.serial.timeout = 5.5
        """_summary_
        """        
        self.modbus_instrument.debug = Debug
        
   
    
    def send(self, Action:Action, start_address:int, count:int = 0,data_list:List = [], text:str = ""):
        try:
            self.modbus_instrument.address = self.address
            if Action == Action.READ_BIT:
                return self.modbus_instrument.read_bit(start_address)
            elif Action == Action.WRITE_BIT:
                self.modbus_instrument.write_bit(start_address)
                return True
            elif Action == Action.READ_BITS:
                return self.modbus_instrument.read_bits(start_address, count)
            elif Action == Action.WRITE_BITS:
                self.modbus_instrument.write_bits(start_address, data_list)
                return True
            elif Action == Action.READ_REGISTER:
                return self.modbus_instrument.read_register(functioncode = 3, registeraddress=start_address,signed = False)
            elif Action == Action.WRITE_REGISTER:
                self.modbus_instrument.write_register(functioncode = 6, registeraddress=start_address,value=data_list[0], signed = False)
                return True
            elif Action == Action.READ_LONG:
                return self.modbus_instrument.read_long(registeraddress=start_address,signed = True)
            elif Action == Action.WRITE_LONG:
                self.modbus_instrument.write_long(registeraddress=start_address,value=data_list[0], signed = True)
                return True
            elif Action == Action.READ_FLOAT:
                return self.modbus_instrument.read_float(registeraddress=start_address,signed = True)
            elif Action == Action.WRITE_FLOAT:
                self.modbus_instrument.write_float(registeraddress=start_address,value=data_list[0], signed = True)
                return True
            elif Action == Action.READ_STRING:
                return self.modbus_instrument.read_string(registeraddress=start_address,number_of_registers = count)
            elif Action == Action.WRITE_STRING:
                self.modbus_instrument.write_string(registeraddress=start_address,textstring = text, number_of_registers = count)
                return True
            elif Action == Action.READ_REGISTERS:
                return self.modbus_instrument.read_registers(registeraddress=start_address,number_of_registers = count)
            elif Action == Action.WRITE_REGISTERS:
                self.modbus_instrument.write_registers(registeraddress=start_address,values = data_list)
                return True
            else:
                print (f'Error, {Action.value} unknown code')

        except Exception as ex:
            #print(str(ex))
            raise Exception(str(ex))

def get_action(cmd:str) -> Action:
    return {
        'rbit': Action.READ_BIT,
        'wbit': Action.WRITE_BIT,
        'rbits': Action.READ_BITS,
        'wbits': Action.WRITE_BITS,
        'rreg': Action.READ_REGISTER,
        'wreg': Action.WRITE_REGISTER,
        'rlong': Action.READ_LONG,
        'wlong': Action.WRITE_LONG,
        'rfloat': Action.READ_FLOAT,
        'wfloat': Action.WRITE_FLOAT,
        'rstr': Action.READ_STRING,
        'wstr': Action.WRITE_STRING,
        'rregs': Action.READ_REGISTERS,
        'wregs': Action.WRITE_REGISTERS
    }[cmd.lower()]

def convert_to_list(i:int) -> list:
    l = []
    x = hex(i)
    x = x[2:]
    last = 0
    


    length = len(x)
    while (length > 0):
        s = min(length, 4)
        if last == 0:
            l.append(int('0x'+x[-s:],16))
            last = -4
                
        else:
            l.append(int('0x'+ x[(last-s):last],16))
            last -= s
        length -= s

    return l

@click.command()
@click.option('--address','-a', type=int, default=250, help='VMA modbus address')
@click.option('--command','-c', type=click.Choice(['rbit', 'wbit', 'rbits', 'wbits', 'rreg', 'wreg', 'rlong','wlong','rfloat','wfloat', 'rstr', 'wstr', 'rregs', 'wregs'], case_sensitive=False), help='Modbus function')
@click.option('--start', '-s', type=int, default = 0, help = 'start register')
@click.option('--count', '-o', type=int, default = 1, help = 'number of registers/bits')
@click.option('--text', '-t', type=str, default = "", help = 'test for write text command')
@click.option('--data', '-d', type= int, multiple=True)
@click.option('--longdata', '-D', type= int, default = 0, help = 'data (for set HWID)')
@click.option('--ComPort', '-P', type=str, help='Comm port name')
@click.option('--Baudrate', '-r', type=int, default = 38400, help='Communication baud rate')
@click.option('--quite', '-q', is_flag=True, help='Do not print results')
@click.option('--Verbose', '-V', is_flag=True, help='Show aditional modbus details')   

def main(address:int, command:str, start:int, count:int, text:str, data, comport:str, baudrate:int, verbose:bool, longdata:int, quite:bool) -> object:
    if comport is None:
        env_comport = os.getenv('RS485_COMPORT')
        if env_comport is not None:
            comport = env_comport
        else:
            comport = '/dev/ttyS2'
    
    if longdata > 0:
        # longdata = hex(longdata)
        data = [0] * count
        cl = convert_to_list(longdata)
        data[0:len(cl)] = cl

    p = ModbusMessage(address=address, Debug=verbose, ComPort=comport, baud_rate = baudrate)
    try:
        r = p.send(Action = get_action(command), start_address = start, count = count, data_list = list(data), text = text)
        print(r)
        #if quite == False:
        #    print (r)
        #else:
        #    return r

    except Exception as ex:
        print (str(ex), file=sys.stderr)
        #if quite == False:
        #    print (str(ex), file=sys.stderr)
        #else:
        #    return str(ex)
    

if __name__ == '__main__':
    main()    
