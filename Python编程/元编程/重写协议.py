# -*- coding: utf-8 -*-
# @Time    : 2018/12/18 10:54
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 重写协议.py
# @Software: PyCharm

def log(cls):
    origin = cls.__getattribute__

    def new_getattribute(self, name):
        print('getting {}'.format(name))
        return origin(self, name)

    cls.__getattribute__ = new_getattribute
    return cls


@log
class A():
    def __init__(self, x):
        self.x = x

    def method(self):
        pass


# a = A(5)
# a.x
# a.method()


class B:
    def __init__(self, age):
        self.age = age

    def __getattr__(self, item):
        print(f'{item}不存在')
        return f'{item}不存在1'

    def __getattribute__(self, item):
        print(f'访问{item}')
        return object.__getattribute__(self, item)

    def test(self):
        print('test 方法')


b = B(8)
b.age
b.test()
print('#' * 100)
print(b.name)
