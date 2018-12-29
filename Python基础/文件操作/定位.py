# -*- coding: utf-8 -*-
# @Time    : 2018/12/28 15:26
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 定位.py
# @Software: PyCharm

f = open('E:\\test.txt', 'r')
con = f.read(5)
print(con)
print(f.tell())
f.seek(12, 0)   # 开头 0  尾部向前 -1
print(f.tell())
con1 = f.read()  # 从12读取
print(con1)
f.close()
