# -*- coding: utf-8 -*-
# @Time    : 2018/12/18 10:38
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 包装函数.py
# @Software: PyCharm

from functools import wraps

def decorate(func):
    @wraps(func)
    def wrapper(*args, debug=False, **kwargs):
        if debug:
            print('call debug')
        return func(*args, **kwargs)
    return wrapper

@decorate
def add(a, b):
    pass

add(3, 4, debug=True)