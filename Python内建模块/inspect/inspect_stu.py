# -*- coding: utf-8 -*-
# @Time    : 2018/12/14 12:59
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : inspect_stu.py
# @Software: PyCharm

from inspect import signature, Parameter, getargspec, getfullargspec


def hello(a, b=1, *k, c, **d):
    pass

sig = signature(hello)
print(sig)  # 获取函数参数
print(sig.parameters)
# print(getargspec(hello))
print(getfullargspec(hello))
print(getfullargspec(hello).args)
for key, value in sig.parameters.items():
    print(key)
    print(value)
    print('属性为：', value.kind)
    print('默认为：', value.default)


b1 = sig.bind(a=1, c=4)
print(b1)


b2 = sig.bind_partial(y=1).arguments  # 判断传入参数是否在 bind 中
print('----------------')
print(b2['d'])
# print(b2)
# if 'd' in b2:
#     print('yes')
#
# for i in b2:
#     print(i)


