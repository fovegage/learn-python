# -*- coding: utf-8 -*-
# @Time    : 2019/1/8 16:12
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 匿名函数2.py
# @Software: PyCharm


a = [1, 2, 3]
x = []
for each in a:
    x.append(each+1)

print(x)


print(list(map(lambda x: x+1, a)))


# 效果一致
def num(x, y):
    return x + y

lambda x, y: x+y



