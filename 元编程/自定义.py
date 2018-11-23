# -*- coding: utf-8 -*-
# @Time    : 2018/11/23 14:37
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 自定义.py
# @Software: PyCharm

from functools import partial, wraps
import logging

def attach_wrap(obj, func=None):
    if func is None:
        return partial(attach_wrap, obj)
    setattr(obj, func.__name__, func)
    return func

# 这层定义参数传递
def log(level, name=None, message=None):

    # 将要传入判定了函数
    def decorate(func):

        # 参数处理
        logname = name if name else func.__name__
        log = logging.getLogger(logname)
        logmess = message if message else func.__name__

        # 函数参入
        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmess)
            return func(*args, **kwargs)

        # 设置参数
        @attach_wrap(wrapper)
        def set_level(newlevel):
            nonlocal level
            level = newlevel

        return wrapper
    return decorate

@log(logging.DEBUG)
def add(a, b):
    return a + b

logging.basicConfig(level=logging.DEBUG)
print(add(3, 5))

add.set_level(logging.WARNING)
print(add(5, 6))


