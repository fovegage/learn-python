# -*- coding: utf-8 -*-
# @Time    : 2018/12/28 14:30
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 引用传参.py
# @Software: PyCharm

# python中使用a = a + a创建了一个新的变量a，覆盖了之前的变量a
# 而使用a += a 则是直接对原变量 a 进行操作

def a(n):
    n += n

n = 1
a(1)
print(n)  # 注意此 n 并没有变化  这里只是对 a 的引用 n 仍为 1  还涉及到作用域变量


list = [1, 2]
a(list)
print(list)  # list 为可变数据类型  故变化