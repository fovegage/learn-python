# -*- coding: utf-8 -*-
# @Time    : 2018/10/25 11:19
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : wraps_stu.py
# @Software: PyCharm

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
