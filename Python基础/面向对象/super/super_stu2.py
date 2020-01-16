# -*- coding: utf-8 -*-
# @Time    : 2018/12/18 16:42
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : super_stu2.py
# @Software: PyCharm

# 在不使用super的继续继承
class A:

    def __new__(cls, *args, **kwargs):
        print(cls, args, kwargs)
        return type("A", (), {})

    def __init__(self):
        print(self)
        self.x = 0

    def add(self):
        pass


class B(A):
    # def __init__(self):
    #     print(f"{self} ---> B")
    #     self.x = 2

    def add(self, n):
        super().add(n)
        pass


b = B()
