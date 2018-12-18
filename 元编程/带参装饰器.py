# -*- coding: utf-8 -*-
# @Time    : 2018/11/23 12:09
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 带参装饰器.py
# @Software: PyCharm
import logging
from functools import wraps

def logged(level, name=None, message=None):
    """
    :param fun:
    :key: name logger name
    :key: level log 等级
    :key： message log信息
    :return:
    """
    def decorate(fun):
        logname = name if name else fun.__module__
        log = logging.getLogger(logname)
        logmessage = message if message else fun.__name__

        @wraps(fun)
        def wrapper(*args, **kwargs):
            log.log(level, logmessage)
            return fun(*args, **kwargs)
        return wrapper
    return decorate

@logged(logging.DEBUG, name='hello')
def add(a, b):
    return a+b

print(add(3, 5))


