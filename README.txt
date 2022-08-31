1. Useing the groups command verify that the user if part of the dailout group.
   if not, add the user to the groups useing:   sudo usermod -aG dailout <user>

2. set an env var called RS485_COMPORT to the serial port in user.
example: export RS485_COMPORT=/dev/ttyS3
         this line can be added at the end of the .bashrc file 


