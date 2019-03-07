# -*- coding: utf-8 -*-
# @Time    : 2019/1/15 9:53
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 实现.py
# @Software: PyCharm

# 图的节点结构
class Node:
    def __init__(self, value):
        self.value = value      # 节点值
        self.come = 0           # 节点入度
        self.out = 0            # 节点出度
        self.nexts = []         # 节点的邻居节点
        self.edges = []         # 在节点为from的情况下，边的集合

# 图的边结构
class Edge:
    def __init__(self, weight, fro, to):
        self.weight = weight        # 边的权重
        self.fro = fro              # 边的from节点
        self.to = to                # 边的to节点

# 图结构
class Graph:
    def __init__(self):
        self.nodes = {}     # 图的所有节点集合  字典形式：{节点编号：节点}
        self.edges = []     # 图的边集合

# 生成图结构
# matrix = [
#   [1,2,3],        ==>   里面分别代表权重, from节点, to节点
#   [...]
# ]

def createGraph(matrix):
    graph = Graph()
    for edge in matrix:
        weight = edge[0]
        fro = edge[1]
        to = edge[2]
        if fro not in graph.nodes:
            graph.nodes[fro] = Node(fro)
        if to not in graph.nodes:
            graph.nodes[to] = Node(to)
        fromNode = graph.nodes[fro]
        toNode = graph.nodes[to]
        newEdge = Edge(weight, fromNode, toNode)
        fromNode.nexts.append(toNode)
        fromNode.out += 1
        toNode.come += 1
        fromNode.edges.append(newEdge)
        graph.edges.append(newEdge)
    return graph

print(createGraph([[1, 2, 3], [2, 3, 4]]))
