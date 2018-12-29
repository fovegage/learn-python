# -*- coding: utf-8 -*-
# @Time    : 2018/12/28 18:55
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 一个for.py
# @Software: PyCharm

a = [i for i in range(10)]
print(a)

b = [i for i in range(10) if i % 2 ==0]
print(b)

list = []
for x in range(3):
    for y in range(3, 6):
        list.append((x, y))

print(list)

# 三轮循环   外层一轮 里层全部
c = [(x, y) for x in range(3) for y in range(3, 6)]
print(c)