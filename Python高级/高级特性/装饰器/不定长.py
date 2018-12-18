# -*- coding: utf-8 -*-
# @Time    : 2018/11/23 11:14
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 不定长.py
# @Software: PyCharm

# 不定长

def C(fun):
    def C_in(*args, **kwargs):
        return args, kwargs

    return C_in

@C
def D(a, b):
    pass

print(D(1, 2, {'x':7}))


from time import ctime, sleep

def timefun(func):  # func 接受函数
    def wrappedfunc(*args):  # *args 接受参数
        print("%s called at %s"%(func.__name__, ctime()))
        func(*args)
    return wrappedfunc

@timefun
def foo(a, b, c):
    print(a+b+c)

foo(3,5,7)
sleep(2)
foo(2,4,9)