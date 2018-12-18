# -*- coding: utf-8 -*-
# @Time    : 2018/11/23 14:37
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 自定义属性装饰器.py
# @Software: PyCharm

from functools import partial, wraps
import logging


def attach_wrap(obj, func=None): # func 判断用
    if func is None:
        return partial(attach_wrap, obj)
    setattr(obj, func.__name__, func)  # obj key value
    print(func.__name__)
    return func   # 返回一个绑定对象

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
        @attach_wrap(wrapper)  # wrapper 为装饰器处理的所有结果
        def set_level(newlevel):
            nonlocal level   # 他将修改全局变量
            level = newlevel

        return wrapper
    return decorate

@log(logging.DEBUG, name='hello')
def add(x, y):
    return x + y


add.set_level(logging.WARN)
print(add(2, 3))