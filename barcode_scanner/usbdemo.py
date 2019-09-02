# FileName : usbdemo.py
# Author   : Adil
# DateTime : 2019/9/1 10:26
# SoftWare : PyCharm

import usb



all_devs = usb.core.find(find_all=True)

print(all_devs)
for d in all_devs:
    if (d.idVendor == 'VID_04F2') & (d.idProduct == 'PID_B541'):
        print(d)





