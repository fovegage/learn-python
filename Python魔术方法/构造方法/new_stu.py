# -*- coding: utf-8 -*-
# @Time    : 2018/11/9 22:33
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : new_stu.py
# @Software: PyCharm

# cls 表示类本身
class inch(float):
    def __new__(cls, args):
        return float.__new__(cls, args*3)

print(inch(12))