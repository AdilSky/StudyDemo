# FileName : demo.py
# Author   : Adil
# DateTime : 2019/9/1 7:03
# SoftWare : PyCharm


import serial
from serial.tools.list_ports_windows import *

plist = list(comports())

if len(plist) <= 0:
    print ("The Serial port can't find!")
else:
    plist_0 =list(plist[0])
    serialName = plist_0[0]
    serialFd = serial.Serial(serialName,9600,timeout = 60)
    print ("check which port was really used >",serialFd.name)






