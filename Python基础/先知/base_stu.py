# -*- coding: utf-8 -*-
# @Time    : 2018/10/24 11:46
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : base_stu.py
# @Software: PyCharm


# [] list
# () tuple
# set {}
# dict {key:value}
# str
# num
# bytes

# 变量命名
# xx: 公有变量
# _x: 单前置下划线,私有化属性或方法，from somemodule import *禁止导入,类对象和子类可以访问  内部实现基本功能函数 可调用
# __xx：双前置下划线,避免与子类中的属性命名冲突，无法在外部直接访问(名字重整所以访问不到)  __name  在继承中是不可以被重写的
# __xx__:双前后下划线,用户名字空间的魔法对象或属性。例如:__init__ , __ 不要自己发明这样的名字  python魔术方法
# xx_:单后置下划线,用于避免与Python关键词的冲突   eg:   is__ 是可以使用的

# foo表示执行函数    foo()  表示带参数执行函数

# 何为可修改类型  即   修改后  内存地址不变

print('' == None)

list = [1, 4, 77]
# 最大值
print(max(list))
# 最小值
print(min(list))

# 计算长度
list = ['a', 'b', 'c']
print(len(list))
