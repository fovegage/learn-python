# -*- coding: utf-8 -*-
# @Time    : 2018/10/18 9:18
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : functions_stu.py
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

# ascii 英文原样输出   汉字输出unicode
# return String
print(ascii('汉字'))

# unicode转汉字
# return String
print(repr("\u6c49\u5b57"))

# bin()  二进制
# return bin
print(bin(6))

# callable  检查函数是否可以被调用
def fun():
    return 3
print(callable(fun))
print(callable(lambda x:3))
print(callable([1,4]))

# chr()  ASCII 码 范围0-255
print(chr(65))

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

# dir()  获取类的方法
print(dir(dict))

# divmod
# return tuple (商, 余数)
print(divmod(5, 3))

# 不满足条件退出
# print(exit())

# format
print("我爱你{}.".format('中国'))
list = ['我', '爱', '你']
print("{0[0]}{0[1]}{0[2]}中国".format(list))
dict = {'name': 'china'}
print("{name}".format(**dict))

# getattr 返回属性值 不存在异常
class B():
    a = 3

print(getattr(B, 'a'))

# globals() 返回当前位置的全部全局变量
print(globals())

# harattr   查找类中是否有属性  没有false 有true
class C():
    a = 3
    b = 4
print(hasattr(C, 'a'))
print(hasattr(C, 'c'))

# hash 返回hash
print(hash(5))

# help  返回方法  tree , dir()  返回方法 list
print(help(list))

# hex 16进制
print(hex(6))

# oct 8进制
print(oct(6))

# 内存地址
print(id(3))

# input 交互
# print(input('请输入'))

# isinstance() 判断是否是已知类型
# return False/True
a = 3
print(isinstance(a, int))

# issubclass() 判断是不是子类
class D():
    a = 1

class E(D):
    b = 2
print(issubclass(E, D))

# ietr() 科迭代对象  到  迭代器
dict = [1, 2, 3]
for i in  iter(dict):
    print(i)

# len 返回字符长度
print(len('我爱你'))