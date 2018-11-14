# -*- coding: utf-8 -*-
# @Time    : 2018/11/8 15:52
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : singlelist.py
# @Software: PyCharm


# 注意指向和赋值的关系 是一样的
class SingleNode():
    def __init__(self, item):
        self.item = item
        self.next = None


class SinleList():
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head == None

    def length(self):
        cur = self._head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        cur = self._head
        while cur != None:
            print(cur.item)
            cur = cur.next

    def headadd(self, item):
        # 实例化一个结点
        node = SingleNode(item)
        # next指向新结点
        node.next = self._head
        # 创建的新结点 赋给第一个结点
        self._head = node

    def tailadd(self, item):
        node = SingleNode(item)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = node


    def insert(self, pos, item):
        if pos <= 0:
            self.headadd(item)
        elif pos >= (self.length()-1):
            self.tailadd(item)
        else:
            count = 0
            node = SingleNode(item)
            pre = self._head
            while count < pos-1:
                count += 1
                pre = pre.next
            # pre.next 原先未断开的指向
            node.next = pre.next
            # 已断开 指向node
            pre.next = node

    def search(self, item):
        cur = self._head
        while cur != None:
            if cur.item == item:
                return True
            cur = cur.next
        return False

    def remove(self, item):
        """删除节点"""
        cur = self._head
        pre = None
        while cur != None:
            # 找到了指定元素
            if cur.item == item:
                # 如果第一个就是删除的节点
                if not pre:
                    # 将头指针指向头节点的后一个节点
                    self._head = cur.next
                else:
                    # 将删除位置前一个节点的next指向删除位置的后一个节点
                    pre.next = cur.next
                break
            else:
                # 继续按链表后移节点
                pre = cur
                cur = cur.next


if __name__ == '__main__':
    s = SinleList()
    s.tailadd(5)
    s.tailadd(6)
    s.tailadd(7)
    s.headadd(1)
    s.insert(1, 100)
    # print(s.length())
    s.travel()
    print(s.search(100))
