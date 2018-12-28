# -*- coding: utf-8 -*-
# @Time    : 2018/11/13 11:33
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 属性.py
# @Software: PyCharm

# 类属性  对象属性
class Person():
    name = 'A'
    _age = '23'
    __len = 180

    def __init__(self):
        self.width = 65

print(Person.name)
# print(Person._age) 类外不可调用
# print(Person.width)  不可访问   类不可访问对象属性
p = Person()
print(p.width)  # 访问对象属性