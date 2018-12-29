# -*- coding: utf-8 -*-
# @Time    : 2018/11/6 11:50
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 迭代器.py
# @Software: PyCharm

# 即常见的数据类型是容器  即可迭代对象
# list,
# set,
# dict,
# tuple,
# str,

# assert
assert 1 in [1, 2, 3]  # 在不报异常  不在异常

# <class 'list'>
# <class 'list_iterator'>
x = [1,2,3]
y = iter(x)
print(type(x))
print(type(y))

# iterator 迭代器才能使用next()  iterable不可使用
# 任何实现了__iter__和__next__()（python2中实现next()）方法的对象都是迭代器
print(next(y))

# 把可迭代对象转成迭代器可以节约内存  用几个取几个  用 next() __next__()
# 它是一个带状态的对象
print(iter([1, 2]))
