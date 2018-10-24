# -*- coding: utf-8 -*-
# @Time    : 2018/10/24 10:26
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : frequ_use_method.py
# @Software: PyCharm


# help  返回方法  tree , dir()  返回方法 list
print(help(list))

# dir()  获取类的方法
print(dir(dict))

# 内存地址
print(id(3))

# format
print("我爱你{}.".format('中国'))
list = ['我', '爱', '你']
print("{0[0]}{0[1]}{0[2]}中国".format(list))
dict = {'name': 'china'}
print("{name}".format(**dict))

# len 返回字符长度  传入str, iter
print(len('我爱你'))

# max  min  *args  iterable
# list首先遍历   lambda 排序规则
print(max(2, 4, 8, 100, 55))
list = [2, 4, 8, 100, 55]
print(max(list, key=str))
# 返回字符串最长的哪个
print(max(list, key=lambda length: len(str(length))))
x = ((3, 5, 8), (3, 8, 5), (3, 6, 9))
print(max(x))
# 只比较下标为 0和2的元素
print(max(x, key=lambda item: (item[0], item[2])))

# ietr() 科迭代对象  到  迭代器
dict = [1, 2, 3]
for i in  iter(dict):
    print(i)

# next
it = iter([1, 2, 3, 4, 5])
# iterator  不可len()
while True:
    try:
        x = next(it)
        print(x, end=',')
    except StopIteration:
        break
# default
for i in range(6):
    print(next(it,'juge'))

# oct 八 bin 二 hex  十六
# oct 八进制
# return oct
print(oct(6))
# bin()  二进制
# return bin
print(bin(6))
# hex 16进制
print(hex(6))

# ord ASCII字符串转换
print(ord('A'))

# chr()  ASCII 码 范围0-255
print(chr(65))

# pow  幂运算
print(pow(2, 3))

# exit() quit()
# exit()/quit()，跑出SystemExit异常。一般在交互式shell中退出时使用

# repr
# unicode转汉字
# return String
print(repr("\u6c49\u5b57"))

# ascii 英文原样输出   汉字输出unicode
# return String
print(ascii('汉字'))

# round   四舍五入截取
print(round(10.4884884, 4))

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

# sorted  reverse key
list = [1, 55, 244, 7, 3]
print(sorted(list, reverse=True))
print(sorted(list, key=lambda x: len(str(x))))

# sum
print(sum([1, 3, 4], 99))

# isinstance() 判断是否是已知类型
# return False/True
a = 3
print(isinstance(a, int))

# divmod
# return tuple (商, 余数)
print(divmod(5, 3))