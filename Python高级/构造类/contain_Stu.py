# -*- coding: utf-8 -*-
# @Time    : 2018/12/21 18:05
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : contain_Stu.py
# @Software: PyCharm

# 我们自定义列表容器

class SortList():
    def __init__(self, initial=None):
        self._item = initial if initial is not None else []

    def __getitem__(self, index):
        return self._item[index]

    # 没有
    def __len__(self):
        return len(self._item)

    def add(self, item):
        import bisect
        bisect.insort(self._item, item)

s = SortList([1, 5, 6])
print(s[2])
print(s.add(99))
print(list(s))
print(len(s))
