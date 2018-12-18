# -*- coding: utf-8 -*-
# @Time    : 2018/12/13 16:23
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 可选参装饰器.py
# @Software: PyCharm
import logging
from functools import partial, wraps


# 用 partial 的原因是  函数可能未初始化  需要绑定参数
def logged(fun=None, * ,level=logging.DEBUG, name=None, message=None):
    if fun is None:
        return partial(logged(logged, level=level, name=name, message=message))

    logname = name if name else fun.__module__
    log = logging.getLogger(logname)
    message = message if message else fun.__name__

    @wraps(fun)
    def wrap(*args, **kwargs):
        log.log(level, message)
        return fun(*args, **kwargs)
    return wrap

# @logged
# def add(x, y):
#     return x+y
#
# print(add(3, 6))


@logged(level=logging.CRITICAL, name='example')
def spam():
    print('Spam!')