# -*- coding: utf-8 -*-
# @Time    : 2018/12/14 14:03
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : exec_stu.py
# @Software: PyCharm

# b 并不是错误
a = 13
exec('b=a+1')
# print(b)

def math():
    a = 13
    loc = locals()
    exec('b=a+1')
    b = loc['b']
    print(b)
    print(loc)


# math()

def math1():
    b = 14
    loc = locals()
    print(loc)
    exec('c=b+3')
    print(loc)
    locals()
    print(loc)

print(math1())


def test3():
    x = 0
    loc = locals()
    print(loc)
    exec('x += 1')
    print(loc)
    locals()
    print(loc)

test3()

