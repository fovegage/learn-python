# -*- coding: utf-8 -*-
# @Time    : 2018/11/23 11:17
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 外部变量.py
# @Software: PyCharm

from time import ctime, sleep

def timefun_arg(pre="hello"):
    def timefun(func):
        def wrappedfunc():
            print("%s called at %s %s"%(func.__name__, ctime(), pre))
            return func()
        return wrappedfunc
    return timefun

@timefun_arg("itcast")
def foo():
    print("I am foo")

@timefun_arg("python")
def too():
    print("I am too")

@timefun_arg()
def too():
    print("I am hello")

foo()
sleep(2)
foo()

too()
sleep(2)
too()