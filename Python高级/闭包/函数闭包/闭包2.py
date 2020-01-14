# -*- coding: utf-8 -*-
# @Time    : 2019/1/8 14:58
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 闭包2.py
# @Software: PyCharm

# 闭包的最大的作用——保存局部信息不被销毁。
# def num(n):
#     num = 1
#     num += n
#     print(num)
#
# i = 0
# while i<5:
#     num(3)
#     i += 1


def num1(n):
    def num_in(i):
        i += i
        print(i)

    return num_in


i = 0
start = num1('start')
while i < 5:
    start(3)
    i += 1


def num2(n):
    i = 1

    def num_in():
        nonlocal i
        i = i + n
        print(i)

    return num_in


i = 0
start = num2(3)
while i < 5:
    start()
    i += 1
