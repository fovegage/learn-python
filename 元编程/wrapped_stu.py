# -*- coding: utf-8 -*-
# @Time    : 2018/11/23 11:53
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : wrapped_stu.py
# @Software: PyCharm

from functools import wraps

# 在我们调试代码的时候  我们使用 wrapped 来取消对函数的装饰
def dec1(fun):
    @wraps(fun)
    def wrapper(*args, **kwargs):
        print('装饰器一')
        return fun(*args, **kwargs)
    return wrapper

def dec2(fun):
    @wraps(fun)
    def wrapper(*args, **kwargs):
        print('装饰器二')
        return fun(*args, **kwargs)  # 必须返回  add 在接受
    return wrapper

@dec1
# @dec2
def add(a, b):
    return a+b

print(add(2, 4))
print('-------------------')
print(add.__wrapped__(2, 3))   # 若被多个装饰器包装  结果不可预知  而被单个装饰器包装  则会直接忽略装饰器