# -*- coding: utf-8 -*-
# @Time    : 2018/9/21 17:26
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : thread_local.py
# @Software: PyCharm

import threading

# 线程不共享局部变量  只共享全局变量
class My_thread(threading.Thread):
    def __init__(self, num):
        threading.Thread.__init__(self)
        self.num = num

    def run(self):
        self.num += 1
        print(self.num)

if __name__ == '__main__':
    t1 = My_thread(1)
    t2 = My_thread(3)
    t1.start()
    t2.start()

