# -*- coding: utf-8 -*-
# @Time    : 2018/12/20 14:30
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : property_stu5.py
# @Software: PyCharm


class lazy():
    def __init__(self, func):
        self.func = func

    # instance 将传入 实例化对象  即 self
    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            value = self.func(instance)
            # print(instance)
            setattr(instance, self.func.__name__, value)
            return value


class area():
    def __init__(self, num):
        self.num = num

    @lazy
    def add(self):
        print('area')
        return self.num + 2



a = area(6)
print(a.add)
del a.add
print(a.add)