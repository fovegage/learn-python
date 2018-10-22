# -*- coding: utf-8 -*-
# @Time    : 2018/10/22 16:22
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : udp_client_stu.py
# @Software: PyCharm

import socket

# 创建套接字
udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 本地地址
localIp = ('192.168.16.1', 10000)

# 发送数据
sendData = input('请输入：')

# 发送数据到目标主机
udpSocket.sendto(sendData.encode(), localIp)

# 接受服务器消息
recvData = udpSocket.recvfrom(1024)

# 输出
print(recvData)

# 关闭套接字
udpSocket.close()
