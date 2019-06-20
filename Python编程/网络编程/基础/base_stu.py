# -*- coding: utf-8 -*-
# @Time    : 2018/10/22 16:15
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : base_stu.py
# @Software: PyCharm

import socket

# AF_INET 用于 Internet 进程间通信
# AF_UNIX 用于同一台机器进程间通信
# SOCK_STREAM 流式套接字，主要用于 TCP 协议
# SOCK_DGRAM  数据报套接字，主要用于 UDP 协议

# tcp
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# udp
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
