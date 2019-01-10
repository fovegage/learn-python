# -*- coding: utf-8 -*-
# @Time    : 2018/12/13 14:22
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 三目运算.py
# @Software: PyCharm

a = 3
b = 4
h = ""

# 若果 a>b 成立  就输出  a-b  否则 a+b
h = a-b if a>b else a+b

print(h)

# 若果 a>b 成立  就输出  a-b  否则 a+b
h1 = a-b and a>b or a+b
print(h1)