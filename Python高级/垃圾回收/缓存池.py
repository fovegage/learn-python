# -*- coding: utf-8 -*-
# @Time    : 2018/12/29 15:08
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 缓存池.py
# @Software: PyCharm


# 以下请在 Python解释下运行  Pycharm 对 Python有做了优化
# [-5, 257)  为python小整数缓存池  即范围内  共享内存

a = 100
b = 100
print(a is b)

c = 58922
d = 58922
print(id(c), id(d))

# 对于相同的字符串也公用内存地址
str1 = 'hello'
str2 = 'hello'
print(id(str1), id(str2))
del str1
del str2

# 删除后引用计数变为1   id 变化
str3 = 'hello'
print(id(str3))

# 加入空格 intern  id 不一致
str4 = 'hello world'
str5 = 'hello world'
print(id(str4), id(str5))
