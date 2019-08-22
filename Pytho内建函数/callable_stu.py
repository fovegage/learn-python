# -*- coding: utf-8 -*-
# @Time    : 2018/12/29 17:17
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : callable_stu.py
# @Software: PyCharm

# callable  检查函数是否可以被调用
def fun():
    return 3
print(callable(fun))
print(callable(lambda x:3))
print(callable([1,4]))
