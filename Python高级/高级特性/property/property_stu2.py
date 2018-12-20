# -*- coding: utf-8 -*-
# @Time    : 2018/12/17 18:50
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : property_stu2.py
# @Software: PyCharm

class Person():
    # Create a property instance
    first_name = property()

    # Apply decorator methods
    @first_name.getter
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value

p = Person()
p.first_name = 'he'
print(p.first_name)