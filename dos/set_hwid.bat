@echo off
setlocal enabledelayedexpansion

set argCount=0
for %%x in (%*) do (
   set /A argCount+=1
)
if %argCount% LSS 8 (
    echo "use set_hwid.bat <16 bit> .... <16 bit>  (8 times)
    goto :EOF
)

python ModbusMessage.py -a 0 -c rregs -s 0 -o 8 -P %RS485_COMPORT% -d %1 -d %2 -d %3 -d %4 -d %5 -d %6 -d %7 -d %8

:EOF