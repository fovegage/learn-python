# -*- coding: utf-8 -*-
# @Time    : 2018/11/14 14:06
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : circulist.py
# @Software: PyCharm

class ListNode():
    '''定义结点'''
    def __init__(self, item):
        self.item = item
        self.next = None

class CircuList():
    '''定义指针'''
    def __init__(self):
        self._head = None

    # 判断链表是否为空
    def is_empty(self):
        return self._head == None

    # 遍历链表
    def travel(self):
        if self.is_empty():
            return
        cur = self._head
        print(cur.item)
        while cur.next != self._head:
            cur = cur.next
            print(cur.item)

    # 链表长度
    def length(self):
        if self.is_empty():
            return 0

        count = 1
        cur = self._head
        while cur.next != self._head:
            count += 1
            cur = cur.next
        return count

    # 头部添加结点
    def headadd(self, item):
        node = ListNode(item)
        if self.is_empty():
            self._head = node
            node.next = self._head

        else:
            # 加入元素指向头结点
            node.next = self._head
            # cur为当前结点  遍历到最后  然后修改指向
            cur = self._head
            while cur.next != self._head:
                cur = cur.next
            cur.next = node
            self._head = node

    # 尾部添加结点
    def tailadd(self, item):
        node = ListNode(item)
        if self.is_empty():
            self._head = node
            node.next = self._head
        else:
            cur = self._head
            while cur.next != self._head:
                cur = cur.next
            cur.next = node
            node.next = self._head

    # 中间插入
    def insert(self, pos, item):
        if pos <= 0:
            self.tailadd(item)
        elif pos >= self.length()-1:
            self.tailadd(item)
        else:
            count = 0
            node = ListNode(item)
            pre = self._head
            while count < pos-1:
                count += 1
                pre = pre.next
            node.next = pre.next
            pre.next = node
    # 搜索
    def search(self, item):
        if self.is_empty():
            return False

        cur = self._head
        if cur.item == item:
            return True

        while cur.next != self._head:
            if cur.item == item:
                return True
            cur = cur.next
        return False
    # 删除
    def remove(self, item):
        """删除一个节点"""
        # 若链表为空，则直接返回
        if self.is_empty():
            return
        # 将cur指向头节点
        cur = self._head
        pre = None
        # 若头节点的元素就是要查找的元素item
        if cur.item == item:
            # 如果链表不止一个节点
            if cur.next != self._head:
                # 先找到尾节点，将尾节点的next指向第二个节点
                while cur.next != self._head:
                    cur = cur.next
                # cur指向了尾节点
                cur.next = self._head.next
                self._head = self._head.next
            else:
                # 链表只有一个节点
                self._head = None
        else:
            pre = self._head
            # 第一个节点不是要删除的
            while cur.next != self._head:
                # 找到了要删除的元素
                if cur.item == item:
                    # 删除
                    pre.next = cur.next
                    return
                else:
                    pre = cur
                    cur = cur.next
            # cur 指向尾节点
            if cur.item == item:
                # 尾部删除
                pre.next = cur.next



if __name__ == '__main__':
    c = CircuList()
    c.headadd(5)
    c.headadd(6)
    c.tailadd(8)
    # print(c.length())
    c.insert(1, 99)
    c.remove(99)
    c.travel()


