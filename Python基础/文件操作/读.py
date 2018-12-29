# -*- coding: utf-8 -*-
# @Time    : 2018/12/28 15:10
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 读.py
# @Software: PyCharm

import os
# 读read
f = open('E:\\test.txt', 'r')
content = f.read(3)  # 指定读取  不指定读取全部
print(content)
print(f.name, f.mode)  # 文件名  模式
f.close()

print('-'*100)

# 读readline()  一次读一行
f = open('E:\\test.txt', 'r')
content = f.readline()
print(content)
f.close()

print("*"*100)

# 读readlines()  全部读出  列表封装
f = open('E:\\test.txt', 'r')
content = f.readlines()
print(content)
f.close()

