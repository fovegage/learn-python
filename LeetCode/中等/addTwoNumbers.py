# -*- encoding: utf-8 -*-

# @File:double.py
# @Author:fovegage
# @Contact:fovegage@gmail.com
# @Created Time:2019/8/23 17:03
# @Version:1.0

"""
给出两个 非空 的链表用来表示两个非负的整数。
其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
"""


class ListNode:
    def __init__(self, item):
        self.val = item
        self.next = None


def gensinglelist1(data):
    """
    顺序插入
    :param data:
    :return:
    """
    # 实例化一个节点
    prenode = ListNode(0)
    lastnode = prenode
    for item in data:
        node = ListNode(item)
        # 尾节点指向刚插入的
        lastnode.next = node
        # 始终是最后一个节点，每加一个
        lastnode = lastnode.next
    return prenode.next


def printlist(l):
    cur = l
    while cur:
        print(cur.val)
        cur = cur.next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        val = l1.val + l2.val
        ansnode = ListNode(val % 10)
        ansnode.next = self.addTwoNumbers(l1.next, l2.next)

        if val >= 10:
            ansnode.next = self.addTwoNumbers(ListNode(1), ansnode.next)
        return ansnode


l1 = gensinglelist1([2, 3, 2])
l2 = gensinglelist1([3, 8, 7])
s = Solution()
printlist(s.addTwoNumbers(l1, l2))
