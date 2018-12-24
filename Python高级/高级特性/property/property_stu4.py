# -*- coding: utf-8 -*-
# @Time    : 2018/12/20 10:55
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : property_stu4.py
# @Software: PyCharm

class Person():
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('must int')
        self._name = value

    @name.deleter
    def name(self):
        raise AttributeError(" cnn't delete")


class Son(Person):

    @property
    def name(self):
        print('Get name')
        return super().name

    @name.setter
    def name(self, value):
        print('set name {}'.format(value))
        super(Son, Son).name.__set__(self, value)

    @name.deleter
    def name(self):
        print('delete name')
        super(Son, Son).name.__delete__(self)

# s = Son('son')
# print(s.name)


# 仅仅设置一个
class sub(Person):
    @Person.name.getter
    def name(self):
        print('get name')
        return super().name

t = sub('hahha')
print(t.name)
