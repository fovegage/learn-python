#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File:node.py 
@Author:fovegage
@Contact:fovegage@gmail.com
@Created Time:2019/8/22 14:34   
@Version:1.0
'''


class ListNode:
    def __init__(self, item):
        self.item = item
        self.next = None


def gensinglelist(data):
    """
    倒序插入
    :param data:
    :return:
    """
    # 初始化头结点
    _head = None
    # 实例化节点
    for item in data:
        node = ListNode(item)
        node.next = _head
        _head = node
    return _head


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
        print(cur.item)
        cur = cur.next


l1 = gensinglelist1([2, 4, 3])
printlist(l1)
