#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File:singlelist.py 
@Author:fovegage
@Contact:fovegage@gmail.com
@Created Time:2019/8/21 15:20   
@Version:1.0
'''


class Node:
    def __init__(self, data):
        """
        创建一个节点，存储数据和下一个数据的指针
        :param data:
        :param next:
        """
        self.data = data
        self.next = None


class SingleList:
    def __init__(self):
        """
        声明头指针
        """
        self._head = None

    def headadd(self, data):
        """
        在链表的头部添加元素，时间复杂度为 1
        :param data:
        :return:
        """
        node = Node(data)
        node.next = self._head  # 把最后一个节点赋值为None或更新指针
        self._head = node  # node会实例化，形成内存地址，将其赋值给头指针

    def travel(self):
        """
        遍历输出单链表，时间复杂度为 n
        :return:
        """
        cur = self._head  # 既是头结点也是头指针
        while cur != None:
            print(cur.data)
            cur = cur.next

    def tailadd(self, data):
        """
        在尾部插入元素，时间复杂度为 n
        :param item:
        :return:
        """
        node = Node(data)
        if self._head is None:
            self._head = None

        cur = self._head
        while cur.next is not None:
            cur = cur.next
        cur.next = node
        node.next = None

    def length(self):
        count = 0
        cur = self._head
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def insert(self, pos, data):
        node = Node(data)
        cur = self._head
        if self._head is None:
            self.headadd(data)

        if self.length() < pos:
            self.tailadd(data)

        else:
            for i in range(1, pos + 1):
                cur = cur.next
            node.next = cur.next
            cur.next = node


s = SingleList()
s.headadd(4)
s.headadd(5)
s.tailadd(7)
s.tailadd(8)
s.insert(3, 6)
s.travel()
print(s.length())
