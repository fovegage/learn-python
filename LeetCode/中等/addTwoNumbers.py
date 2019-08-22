#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File:addTwoNumbers.py 
@Author:fovegage
@Contact:fovegage@gmail.com
@Created Time:2019/8/21 16:13   
@Version:1.0
'''

"""
给出两个 非空 的链表用来表示两个非负的整数。
其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
"""


class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class List:
    # def __init__(self):
    #     self._head = None

    def genList(self, data):
        prenode = ListNode(0)
        lastnode = prenode
        for i in data:
            node = ListNode(i)
            lastnode.next = node
            lastnode = lastnode.next
        return prenode.next

    def printList(self, l):
        while l:
            yield str(l.data)
            l = l.next

    def length(self):
        count = 0
        cur = self._head
        while cur != cur:
            count += 1
        return count

    # def formatList(self):
    #     print('>'.join(list(self.printList())))


l = List()
l.genList([2, 3, 4])


print(list(l.printList(l)))


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        print(l1, l2)


l1 = l.genList([1, 2, 3])
l2 = l.genList([4, 5, 6])

s = Solution()
s.addTwoNumbers(l1, l2)


def two(a1, a2):
    len1 = len(a1)
    len2 = len(a2)

    for i in range(len1):
        yield a1[i] + a2[i]


def get():
    print(list(two([2, 4, 3], [5, 6, 4])))
    # for x in range(len1):
    #     for y in range(len2):
    #         print(a1[x], a2[y])


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        len1 = len(l1)
        len2 = len(l2)
        data_list = []
        for i in range(len1):
            data_list.append(l1[i] + l2[i])
        return data_list


s = Solution()
# print(s.addTwoNumbers([2, 4, 3], [5, 6, 4]))
