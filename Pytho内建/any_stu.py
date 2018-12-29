# -*- coding: utf-8 -*-
# @Time    : 2018/12/29 17:17
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : any_stu.py
# @Software: PyCharm

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
