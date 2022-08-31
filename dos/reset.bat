@echo off
setlocal enabledelayedexpansion

set argCount=0
for %%x in (%*) do (
   set /A argCount+=1
)
if %argCount% LSS 1 (
    echo "use reset.bat <address>
    goto :EOF
)

python ..\ModbusMessage.py -a %1 -c wreg -s 52 -d 1 -P %RS485_COMPORT%

:EOF
