# -*- coding: utf-8 -*-
# @Time    : 2019/1/7 17:27
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 应注意.py
# @Software: PyCharm

class Perosn():
    name = 'Gage'

p1 = Perosn()
p2 = Perosn()
print(p1.name)
p2.name = 'hello'
print(p2.name)
print(p1.name)
print(Perosn.name)


class Perosn():
    name = []

p1 = Perosn()
p2 = Perosn()
p2.name.append('hello')
print(p2.name)
print(p1.name)
print(Perosn.name)