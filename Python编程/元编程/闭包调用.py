# -*- coding: utf-8 -*-
# @Time    : 2018/12/18 10:08
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 闭包调用.py
# @Software: PyCharm

from functools import partial, update_wrapper, WRAPPER_ASSIGNMENTS, WRAPPER_UPDATES


def wraps(wrapped,
          assigned=WRAPPER_ASSIGNMENTS,
          updated=WRAPPER_UPDATES):
    return partial(update_wrapper, wrapped=wrapped,
                   assigned=assigned, updated=updated)


def decorate(func):
    num = 0

    @wraps(func)
    def wrpper(*args, **kwargs):
        nonlocal num
        num += 1
        return func(*args, **kwargs)

    wrpper.num = lambda: num
    return wrpper


@decorate
def add(a, b):
    return a + b


add(2, 4)
print(add.num())
