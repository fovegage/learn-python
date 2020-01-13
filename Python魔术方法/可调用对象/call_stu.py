# -*- coding: utf-8 -*-
# @Time    : 2018/11/28 11:31
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : call_stu.py
# @Software: PyCharm

#  可调用对象
class A():
    def __call__(self, a):
        self.a = a
        print(self.a)

    def print(self):
        print(self.a)


t = A()
t(5)
print(t.__dict__)


# t.print()

class Entity():

    def __init__(self, size, x, y):
        self.x, self.y = x, y
        self.size = size

    def __call__(self, x, y):
        '''改变实体的位置'''
        self.x, self.y = y, x
        print(self.x, self.y)


e = Entity(3, 4, 3)
e(3, 5)  # e.__call__(3, 5)  两者作用一样

print(e.__dict__)


class Fab:

    # def __init__(self, start):
    #     self.start = start

    def __call__(self, *args, **kwargs):
        print(args)
        a, b = 0, 1
        self.list = []
        for i in range(*args, **kwargs):
            self.list.append(b)
            a, b = b, a + b
        return self.list

    # def __str__(self):
    #     return self.list


print(Fab()(10))
# f = Fab()
# print(f(10))
