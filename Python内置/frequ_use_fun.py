# -*- coding: utf-8 -*-
# @Time    : 2018/10/24 11:50
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : frequ_use_fun.py
# @Software: PyCharm

# zip  iter --> tuple
list1 = [1, 2, 3, 5]
list2 = [4, 5, 6]
zipped = zip(list1, list2)
print(list(zipped))  # 为节省内存   返回obj  list取出 [(1, 4), (2, 5), (3, 6)]
# print(list(zip(*zipped)))  # [(1, 2, 3), (4, 5, 6)]

# type()
print(type(3))

# super()

# staticmethod()

# slice()

# reversed()
bool
# range()

# property()

# memoryview()

# map()  [3, 6, 9]  返回map对象  即迭代器
l = map(lambda x:x*3, [1, 2, 3])
print(list(l))


# frozenset()

# filter()

# enumerate()

# complex()

# classmethod()

# bytes()

# bytearray()

# bool

# float()
@staticmethod
def d():
    pass

# int

# str



