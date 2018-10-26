# -*- coding: utf-8 -*-
# @Time    : 2018/10/25 11:19
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : decorator_stu.py
# @Software: PyCharm
from functools import wraps
# 无参数
def makeBold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped

@makeBold
def test1():
    return "hello world-1"

print(test1())

# 有参数
def A(fun):
    def A_in(a, b):
        fun(a, b)
        return a*b
    return A_in

@A
def B(a, b):
    print(a+b)

print(B(3, 4))

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

def timefun(func):
    def wrappedfunc(*args):
        print("%s called at %s"%(func.__name__, ctime()))
        func(*args)
    return wrappedfunc

@timefun
def foo(a, b, c):
    print(a+b+c)

foo(3,5,7)
sleep(2)
foo(2,4,9)


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

from functools import wraps


def logged(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)

    return with_logging


@logged
def f(x):
    """does some math"""
    return x + x * x


print(f.__name__)  # prints 'f'
print(f.__doc__)  # prints 'does some math'
print(f(5))
