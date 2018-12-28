# -*- coding: utf-8 -*-
# @Time    : 2018/12/28 9:00
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 函数类型.py
# @Software: PyCharm


# 无参数，无返回值的函数
def sayHello():
    print('hello')

sayHello()

# 无参数，有返回值的函数
def num():
    return 1

num = num()
print(num)

# 有参数，无返回值的函数
def add(a, b):
    # 比如向数据库写入数据，无需返回，若异常会报错
    ...

# 有参数，有返回值的函数
def sum(n):
    ret = 0
    i = 0
    while i <= n:
        ret = ret +i
        i += 1

    return ret

ret = sum(100)
print(ret)