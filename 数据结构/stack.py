# -*- coding: utf-8 -*-
# @Time    : 2018/11/16 15:39
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : stack.py
# @Software: PyCharm

class Stack():
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def length(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self, item):
        self.items.pop(item)

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return self.items


s = Stack()
s.push(9)
print(s.is_empty())