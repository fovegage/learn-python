# -*- coding: utf-8 -*-
# @Time    : 2018/10/18 10:05
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 匿名函数.py
# @Software: PyCharm


# lambda [arg1 [,arg2,.....argn]]:expression

fun1 = lambda x, y: x * y
print(fun1(2, 3))


def fun2(x, y):
    return x * y


print(fun2(2, 3))

l = lambda: 5
print(l())

stus = [
    {"name": "zhangsan", "age": 18},
    {"name": "lisi", "age": 19},
    {"name": "wangwu", "age": 17}
]

# key 相当于 item
stus.sort(key=lambda x: len(x['name']))
stus.sort(key=lambda x: x['age'])
print(stus)
