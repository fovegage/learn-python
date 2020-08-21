# -*- coding: utf-8 -*-
# @Time    : 2018/11/13 14:32
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : iter协议.py
# @Software: PyCharm

# 迭代器必须遵循迭代器协议，需要有 __iter__ (返回它本身) 和 next

"""
实现 __next__ 访问完就会被销毁
"""
class iterH:

    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return self

    def __next__(self):
        if self.data > 5:
            raise StopIteration
        else:
            self.data += 1
            return self.data


# print(type(iterH))
# for i in iterH(3):
#     print(i)

class IterDemo:
    def __init__(self):
        self.count = 1

    def __iter__(self):
        print(self)
        return self

    def __next__(self):
        if self.count < 10:
            self.count += 1
            return self.count
        else:
            raise StopIteration

it = IterDemo()
# print(list(it))
# print(list(it))
