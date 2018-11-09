# -*- coding: utf-8 -*-
# @Time    : 2018/11/8 15:52
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : singlelist.py
# @Software: PyCharm

class SingleNode():
    def __init__(self, item):
        self.item = item
        self.next = None


class SinleList():
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head == None

    def add(self, item):
        node =SingleNode(item)
        node.next = self._head
        self._head = node

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
    s.add(1)
    s.remove(1)
    s.add(2)
    print(s.is_empty())