# -*- coding: utf-8 -*-
# @Time    : 2018/12/18 16:42
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : super_stu2.py
# @Software: PyCharm

class A():
    def __init__(self):
        self.x = 0

class B(A):
    def __init__(self):
        super().__init__()  # 保证父类初始化
        self.y = 1