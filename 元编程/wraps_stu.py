# -*- coding: utf-8 -*-
# @Time    : 2018/11/23 11:08
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : wraps_stu.py
# @Software: PyCharm

import time
from functools import wraps
from inspect import signature

# wraps 可以完整的保留所参入函数的所有信息
def task(fun):
    """使用wraps接受函数"""
    @wraps(fun)
    def execute(*args, **kwargs):
        start = time.time()
        ret = fun(*args, **kwargs)
        end = time.time()
        print(fun.__name__, end-start)
        return ret
    return execute

@task
def love(n):
    """文档说明"""
    while n > 0:
        n -= 1

love(10000000)
print(love.__module__)
print(love.__name__)
print(love.__doc__)  # 如果不使用 wraps 将不可以获取到注释信息和签名信息
print(love.__annotations__)

# 显示参数信息
print(signature(love))



