# -*- coding: utf-8 -*-
# @Time    : 2018/11/15 17:34
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : doublelist.py
# @Software: PyCharm

# 定义头结点
class Node():
    def __init__(self, item):
        # 定义元素
        self.item = item
        # 定义前驱指针
        self.prev = None
        # 定义后继指针
        self.next = None

class DoubleList():
    # 定义头指针
    def __init__(self):
        self._head = None


    def is_empty(self):
        return self._head == None

    def length(self):
        if self.is_empty():
            return 0

        cur = self._head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        cur = self._head
        while cur is not None:
            print(cur.item)
            cur = cur.next

    def search(self, item):
        if self.is_empty():
            return False

        cur = self._head
        while cur is not Node:
            if cur.item == item:
                return True
            cur = cur.next
        return False

    def headadd(self, item):
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            node.next = self._head
            self._head.prev = node
            self._head = node

    def tailadd(self, item):
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next is not None:
                cur = cur.next
            cur.next = node
            node.prev = cur


if __name__ == '__main__':
    d = DoubleList()
    print(d.length())
    d.headadd(88)
    d.headadd(9)
    d.tailadd(678)
    d.travel()
    print(d.search(88))
