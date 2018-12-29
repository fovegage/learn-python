# -*- coding: utf-8 -*-
# @Time    : 2018/12/28 18:06
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 类属性.py
# @Software: PyCharm

class People(object):
    name = 'Tom'  #公有的类属性
    __age = 12     #私有的类属性

p = People()

print(p.name)           #正确
print(People.name)      #正确
# print(p.__age)            #错误，不能在类外通过实例对象访问私有的类属性
# print(People.__age)        #错误，不能在类外通过类对象访问私有的类属性