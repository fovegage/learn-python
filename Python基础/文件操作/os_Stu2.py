# -*- coding: utf-8 -*-
# @Time    : 2018/12/28 15:49
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : os_Stu2.py
# @Software: PyCharm
import os

print(os.cpu_count())

print(os.getpid()) # 当前进程

print(os.getppid()) # 父进程

# print(os.system())  # 执行系统命令

print(list(os.scandir('E:\\')))  # 返回迭代器 next 取值



#  head tail  ('D:\\Users\\foveg\\AppData\\Local\\Programs\\Python\\Python36', 'Lib')
print(os.path.split('D:\\Users\\foveg\\AppData\\Local\\Programs\\Python\\Python36\\Lib'))

# 转换path的大小写和斜杠  d:\users\foveg\appdata
print(os.path.normcase('D:\\Users\\foveg\\AppData'))

# 判断是否绝对路径  True
print(os.path.isabs('E:\\'))

# 拼接路径 并不对路径做真实判断  E:\love\hello
print(os.path.join('E:\\love', 'hello'))

# ('D:', '\\Users\\foveg\\AppData')
print(os.path.splitdrive('D:\\Users\\foveg\\AppData'))


# ('D:\\Users\\foveg\\AppData\\a', '.py')  识别扩展名
print(os.path.splitext('D:\\Users\\foveg\\AppData\\a.py'))
