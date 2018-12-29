# -*- coding: utf-8 -*-
# @Time    : 2018/10/22 17:47
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : tcp_server_stu.py
# @Software: PyCharm

import socket

# 链接
tcpserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定本地端口信息   即服务器端口
bindip = ('', 8888)
tcpserver.bind(bindip)

# 监听
tcpserver.listen(5)

# 子链接
childsocket, ip = tcpserver.accept()

# 接受
data = childsocket.recv(1024)
print(data, ip)

# 发送
childsocket.send('love'.encode())

# 关闭
childsocket.close()
tcpserver.close()
