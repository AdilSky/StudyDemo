# FileName : test.py
# Author   : Adil
# DateTime : 2019/9/1 7:25
# SoftWare : PyCharm


import serial


ser = serial.Serial('COM6', 9600,timeout=0.5)
# ser = serial.Serial('COM6', 9600)

print(ser.name)

print(ser.port)

if not ser.isOpen():
    ser.open()
    print('com3 is open', ser.isOpen())



# 获取一行信息
def recv(serial):
    print('2')
    data = ''
    while serial.inWaiting() > 0:
        print(serial.inWaiting())
        print('3')
        # data += str(serial.read(15)) # ok 要配合timeout 使用, 否则要传入已知 的 size
        # data += str(serial.readline())  # ok 要配合timeout 使用
        # data += str(serial.readlines())  # ok 要配合timeout 使用
        # data += str(serial.readall())     # ok 要配合timeout 使用
        data += str(serial.read_all())    # ok 要配合timeout 使用

        print("************************************")
        #print(serial.read(13))
        print('准备打印data')
        # data = str(serial.read(19))
        print(data)
        print('data:%s'%data)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    return data



# cursor.execute("DROP TABLE IF EXISTS productinfo")

'''
sql="""CREATE TABLE productinfo(
        code  CHAR(18),
        price double(9,2),
        info  CHAR(25))"""
cursor.execute(sql)
'''

sum = 0.0
while True:
    print('1')
    data = recv(ser)
    print('4')
    if data != '':
        print('5')
        print(data)
        break


ser.close()




