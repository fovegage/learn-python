# -*- coding:utf-8 -*-
# Author:Wong Du

import socket
import time

server_addr = ("localhost", 9000)
client_socket = [socket.socket() for i in range(100)]

msg_data = "如果我是dj，你会爱我吗？"
count = 0


for client in client_socket:
    try:
        client.connect(server_addr)
        print("Success to connected...")
        client.send(msg_data.encode())
        data = client.recv(1024)
        print(data.decode())
        count += 1
    except ConnectionResetError:
        print(count)
time.sleep(10)

