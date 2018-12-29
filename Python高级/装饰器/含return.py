# -*- coding: utf-8 -*-
# @Time    : 2018/11/23 11:16
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 含return.py
# @Software: PyCharm

from time import ctime, sleep

def timefun(func):
    def wrappedfunc():
        print("%s called at %s"%(func.__name__, ctime()))
        func()
    return wrappedfunc

@timefun
def foo():
    print("I am gage")

@timefun
def getInfo():
    return '----hahah---'

foo()
sleep(2)
foo()