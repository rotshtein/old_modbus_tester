@echo off
setlocal enabledelayedexpansion


set argCount=0
for %%x in (%*) do (
   set /A argCount+=1
)
if %argCount% LSS 1 (
    echo "use close_valve.bat <address>
    goto :EOF
)

python ..\ModbusMessage.py -a %1 -c wreg -s 24 -d 3 -P %RS485_COMPORT%


:EOF
