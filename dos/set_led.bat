@echo off
setlocal enabledelayedexpansion

set argCount=0
for %%x in (%*) do (
   set /A argCount+=1
)
if %argCount% LSS 2 (
    echo "use set_led.bat <address>
    goto :EOF
)

python ..\ModbusMessage.py -a %1 -c wreg -s 28 -d %s -P %RS485_COMPORT%


:EOF