# -*- coding: utf-8 -*-
# @Time    : 2018/12/28 18:07
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 实列属性.py
# @Software: PyCharm

class People(object):
    address = '山东' #类属性
    def __init__(self):
        self.name = 'xiaowang' #实例属性
        self.age = 20 #实例属性

p = People()
p.age =12 #实例属性
print(p.address) #正确
print(p.name)    #正确
print(p.age)     #正确

print(People.address) #正确
# print(People.name)    #错误
# print(People.age)     #错误