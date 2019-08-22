# -*- coding: utf-8 -*-
# @Time    : 2018/12/29 16:54
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : memoryview_Stu.py
# @Software: PyCharm

# 查看在内存中的形态

a = memoryview(bytearray('abcdeg', encoding='utf-8'))
print(a[1])
print(a)
print(a[1:4])