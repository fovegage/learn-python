# -*- coding: utf-8 -*-
# @Time    : 2018/11/6 10:20
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : yeild_stu.py
# @Software: PyCharm


# yeild 和return
# 1  不具备调用性
def fun1(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b, end=',')
        a, b = b, a+b
        n += 1

print(fun1(5))

# 2  升级版
def fun2(max):
    n, a, b = 0, 0, 1
    list = []
    while n < max:
       list.append(b)
       a, b = b, a+b
       n += 1
    return list

print(fun2(5))

# 3 任何实现了__iter__和__next__()（python2中实现next()）方法的对象都是迭代器
class Fab(object):

    def __init__(self, max):
        self.max = max
        self.n, self.a, self.b = 0, 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.n < self.max:
            r = self.b
            self.a, self.b = self.b, self.a + self.b
            self.n = self.n + 1
            return r
        raise StopIteration()

next(Fab(5))
for i in Fab(5):
    print(i)

# 4   yield把一个函数变成生成器 调用 fab(5) 不会执行 fab 函数，而是返回一个 iterable 对象
# 每遇到yield返回一个迭代值
print('*'*20)
def fun3(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n += 1

for i in fun3(5):
    print(i)


import types
print(isinstance(fun3(6), types.GeneratorType))
import collections
print(isinstance(fun3(6), collections.Iterable))


# yield与return 联用
def read_file(fpath):
   BLOCK_SIZE = 1024
   with open(fpath, 'rb') as f:
       while True:
           block = f.read(BLOCK_SIZE)
           if block:
               yield block
           else:
               return