# -*- coding: utf-8 -*-
# @Time    : 2018/12/21 13:03
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : bind_stu.py
# @Software: PyCharm

# 定义基类
# self 类本身
class Base():
    def __init__(self, name, **par):
        self.name = name
        for key, value in par.items():
            setattr(self, key, value)

    def __set__(self, instance, value):
        if instance is None:
            return self
        else:
            instance.__dict__[self.name] = value

# 定义检查类
class MsutInt(Base):
    expect_type = type(None)
    def __set__(self, instance, value):
        if not isinstance(value, self.expect_type):
            raise TypeError('must is {}'.format(self.expect_type))
        super().__set__(instance, value)


# 定义数据类型
class Interger(MsutInt):
    expect_type = int


class Stock():
    age = Interger('age')

    def __init__(self, age):
        self.age = age


s = Stock(24)
print(repr(s.age))

# 使用元类

class check(type):
    def __new__(cls, clsname, bases, methods):
        # Attach attribute names to the descriptors
        for key, value in methods.items():
            if isinstance(value, Base):
                value.name = key
        return type.__new__(cls, clsname, bases, methods)

class Stock1(metaclass=check):
    age = Interger('age')

    def __init__(self, age):
        self.age = age


s = Stock1(23)
print(repr(s.age))



