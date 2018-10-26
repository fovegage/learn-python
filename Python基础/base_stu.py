# -*- coding: utf-8 -*-
# @Time    : 2018/10/24 11:46
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : base_stu.py
# @Software: PyCharm

# 变量命名
# xx: 公有变量
# _x: 单前置下划线,私有化属性或方法，from somemodule import *禁止导入,类对象和子类可以访问
# __xx：双前置下划线,避免与子类中的属性命名冲突，无法在外部直接访问(名字重整所以访问不到)
# __xx__:双前后下划线,用户名字空间的魔法对象或属性。例如:__init__ , __ 不要自己发明这样的名字
# xx_:单后置下划线,用于避免与Python关键词的冲突

# 普通运算符
# + - * / // % **
print(2+3)
print(2-3)
print(2*3)
print(2/3)  # 商
print(2//3) # 不带余数商
print(2**3) # 幂

# 比较运算符 <> python3 取消
print(3 != 5)

# 逻辑运算符  or and not
print(not 3)

# 集  只能是集合  set()
# & 交集  | 并集  - 差集
# x^z #对称差集(在x或z中，但不会同时出现在二者中)
print({1, 3, 4} & {2, 4})


