# -*- coding: utf-8 -*-
# @Time    : 2018/12/14 12:57
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 类型检验.py
# @Software: PyCharm

from inspect import signature
from functools import wraps

def typeassert(*ty_args, **ty_kwargs):
    def decorate(func):
        # If in optimized mode, disable type checking
        if not __debug__:
            return func

        # Map function argument names to supplied types
        sig = signature(func)
        # 绑定设定的
        bound_types = sig.bind_partial(*ty_args, **ty_kwargs).arguments
        print(bound_types)

        @wraps(func)
        def wrapper(*args, **kwargs):
            # 绑定传入的
            bound_values = sig.bind(*args, **kwargs)
            # Enforce type assertions across supplied arguments
            for name, value in bound_values.arguments.items():
                print(name, value)
                if name in bound_types:
                    if not isinstance(value, bound_types[name]):

                        raise TypeError(
                            'Argument {} must be {}'.format(name, bound_types[name])
                        )
            return func(*args, **kwargs)

        return wrapper
    return decorate



@typeassert(int, z=int)
def heelo(x, y, z=42):
    print(x, y, z)

heelo(1, 5 , 6)

