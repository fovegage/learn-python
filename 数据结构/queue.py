# -*- coding: utf-8 -*-
# @Time    : 2018/11/16 15:46
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : queue.py
# @Software: PyCharm

class Queue():
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def inqueue(self, item):
        self.items.insert(0, item)

    def outqueue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

q = Queue()
print(q.inqueue(99))