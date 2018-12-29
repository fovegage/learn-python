# -*- coding: utf-8 -*-
# @Time    : 2018/10/22 17:00
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : udp_server_stu.py
# @Software: PyCharm

import socket

# 创建
udpsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定ip  只接受6008的客户端ip
bindip = ('', 6008)
udpsocket.bind(bindip)


# 接收数据
while True:
    recvdata = udpsocket.recvfrom(1024)
    print(recvdata)


# 关闭
udpsocket.close()