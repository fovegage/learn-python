# -*- coding: utf-8 -*-
# @Time    : 2018/10/18 9:18
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : nofrequ_use_method.py
# @Software: PyCharm

# functions

# abs() 返回绝对值
# return int
print(abs(-5))

# all()  0 Null False 为 false  其他是True
# 在iterable中如果存在 0 Null False 返回 False 否则返回True
# 如果是空，返回True
# return False/True
print(all([0, 1, 2, 3]))
print(all([1, 2, 3]))
print(all([]))

# any()  与all()相反
# return False/True
print(any(()))

# callable  检查函数是否可以被调用
def fun():
    return 3
print(callable(fun))
print(callable(lambda x:3))
print(callable([1,4]))

# compile()  编译字符代码  必须借助于 exec() 和 eval()
# exec()  动态执行代码块
# eval()   执行表达式
str = "for i in range(5): print(i)"
print(compile(str, '<int>', 'exec'))
exec(compile(str, '', 'exec'))

# copyright python版权声明
print(copyright())

# 详细python版权声明
print(credits())

# hash 返回hash
print(hash(5))

# input 交互
# print(input('请输入'))

# issubclass() 判断是不是子类
class D():
    a = 1
class E(D):
    b = 2
print(issubclass(E, D))

# globals() 返回当前位置的全部全局变量
print(globals())

# locals  获取局部变量
print(locals())

# vars() 函数返回对象object的属性和属性值的字典对象
print(vars())