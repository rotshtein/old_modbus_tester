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

python ..\ModbusMessage.py -a 0 -c rregs -s 0 -o 8 -P %RS485_COMPORT% -D %1