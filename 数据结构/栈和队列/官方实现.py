# -*- coding: utf-8 -*-
# @Time    : 2019/6/6 11:02
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 官方实现.py
# @Software: PyCharm

import queue


# 先进先出
FIFO = queue.Queue()

for i in range(5):
    FIFO.put(i)  # 用于生产

print(FIFO.get())  # 用于消费
print(FIFO.qsize()) # 队列大小
print(FIFO.full()) # 队列是否满

