# -*- coding: utf-8 -*-
# @Time    : 2018/12/17 19:04
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : types_stu.py
# @Software: PyCharm

import types

print(dir(types))

def func():
    pass

print(isinstance(func, types.FunctionType))


# 动态添加方法

class Foo():
    def l1(self):
        print('l1')

def l2(self):
    print('l2')

f = Foo()
f.l2 = types.MethodType(l2, f)  # 可以动态绑定
f.l2()