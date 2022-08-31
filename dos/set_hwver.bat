@echo off
setlocal enabledelayedexpansion

set argCount=0
for %%x in (%*) do (
   set /A argCount+=1
)
if %argCount% LSS 2 (
    echo "use open_valve.bat <address>
    goto :EOF
)

python ..\ModbusMessage.py -a %1 -c wreg -s 34 -d %2 -P %RS485_COMPORT%


:EOF