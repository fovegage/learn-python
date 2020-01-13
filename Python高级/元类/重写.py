# -*- coding: utf-8 -*-
# @Time    : 2019/1/7 16:05
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 重写.py
# @Software: PyCharm

# __new__ 是在__init__之前被调用的特殊方法，__new__是用来创建对象并返回之的方法，__new_()是一个类方法
# 而__init__只是用来将传入的参数初始化给对象，它是在对象创建之后执行的方法。

class UpperAtrr(type):
    def __new__(cls, future_class_name, future_class_parents, future_class_attr):
        attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))
        upper_attr = dict((name.upper(), value) for name, value in attrs)
        # return type(future_class_name, future_class_parents, upper_attr)
        # return type.__new__(cls, future_class_name, future_class_parents, upper_attr)
        return super(UpperAtrr, cls).__new__(cls, future_class_name, future_class_parents, upper_attr)


class A(metaclass=UpperAtrr):
    bar = 'bip'


print(hasattr(A, 'bar'))
print(A.BAR)
