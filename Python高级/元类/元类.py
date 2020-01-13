# -*- coding: utf-8 -*-
# @Time    : 2018/12/14 15:04
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 元类.py
# @Software: PyCharm

# () 内为 继承的类名称  {} 为  方法或属性
foo = type('Foo', (), {})
print(foo)
print(foo())

class B:
    pass


class A(foo):
    pass


print(foo.__mro__)
