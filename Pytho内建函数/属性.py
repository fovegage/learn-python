# -*- coding: utf-8 -*-
# @Time    : 2018/10/24 10:26
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 属性.py
# @Software: PyCharm



























# getattr 返回属性值 不存在异常
class B():
    a = 3

print(getattr(B, 'a'))

# setattr
setattr(B, 'b', 18)
print(B().b)

# harattr   查找类中是否有属性  没有false 有true
class C():
    a = 3
    b = 4
print(hasattr(C, 'a'))
print(hasattr(C, 'c'))

# delattr() 删除类属性
class cl():
    a = 3
    b = 4

print(cl().a, cl().b)
delattr(cl, 'a')
try:
    print(cl().a, cl().b)
except:
    print('a被删除了')



