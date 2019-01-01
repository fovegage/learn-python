# -*- coding: utf-8 -*-
# @Time    : 2018/11/16 16:14
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : tree.py
# @Software: PyCharm

class Node():
    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild

class Tree():
    def __init__(self, root=None):
        self.root = root

    def is_empty(self):
        return self.root == None

    def add(self, elem):
        """为树添加节点"""
        node = Node(elem)
        # 如果树是空的，则对根节点赋值
        if self.root == None:
            self.root = node
        else:
            queue = []
            queue.append(self.root)
            # 对已有的节点进行层次遍历

            while queue:
                # 弹出队列的第一个元素
                cur = queue.pop(0)
                if cur.lchild == None:
                    cur.lchild = node
                    return
                elif cur.rchild == None:
                    cur.rchild = node
                    return
                else:
                    # 如果左右子树都不为空，加入队列继续判断
                    queue.append(cur.lchild)
                    queue.append(cur.rchild)
t = Tree()
t.add(5)
t.add(6)
t.add(7)