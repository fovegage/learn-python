# -*- coding: utf-8 -*-
# @Time    : 2018/11/13 11:33
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 属性.py
# @Software: PyCharm


# 变量命名
# xx: 公有变量
# _x: 单前置下划线,私有化属性或方法，from somemodule import *禁止导入,类对象和子类可以访问  内部实现基本功能函数 可调用
# __xx：双前置下划线,避免与子类中的属性命名冲突，无法在外部直接访问(名字重整所以访问不到)  __name  在继承中是不可以被重写的
# __xx__:双前后下划线,用户名字空间的魔法对象或属性。例如:__init__ , __ 不要自己发明这样的名字  python魔术方法
# xx_:单后置下划线,用于避免与Python关键词的冲突   eg:   is__ 是可以使用的


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