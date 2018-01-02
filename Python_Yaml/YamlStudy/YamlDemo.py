# FileName : YamlDemo.py
# Author   : Adil
# DateTime : 2017/12/29 12:00
# SoftWare : PyCharm

import yaml
import os

# 获取当前文件路径 D:/WorkSpace/StudyPractice/Python_Yaml/YamlStudy
filePath = os.path.dirname(__file__)
print(filePath)
# 获取当前文件的Realpath  D:\WorkSpace\StudyPractice\Python_Yaml\YamlStudy\YamlDemo.py
fileNamePath = os.path.split(os.path.realpath(__file__))[0]
print(fileNamePath)
# 获取配置文件的路径 D:/WorkSpace/StudyPractice/Python_Yaml/YamlStudy\config.yaml
yamlPath = os.path.join(fileNamePath,'config.yaml')
print(yamlPath)
# 加上 ,encoding='utf-8'，处理配置文件中含中文出现乱码的情况。
f = open(yamlPath,'r',encoding='utf-8')

cont = f.read()

x = yaml.load(cont)
print(type(x))
print(x)
print(x['EMAIL'])
print(type(x['EMAIL']))
print(x['EMAIL']['Smtp_Server'])
print(type(x['EMAIL']['Smtp_Server']))
print(x['DB'])
print(x['DB']['host'])

print(x.get('DB').get('host'))

print(type(x.get('DB')))



