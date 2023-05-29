# -*- coding: utf-8 -*-
# @Time    : 2018/9/21 17:37
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : thread_syn.py
# @Software: PyCharm

import threading


# 为实现同步  一边锁  一边释放
class My_thread_1(threading.Thread):
    def run(self):
        while True:
            if l1.acquire():
                print("task1")
                l2.release()


class My_thread_2(threading.Thread):
    def run(self):
        while True:
            if l2.acquire():
                print("task2")
                l3.release()


class My_thread_3(threading.Thread):
    def run(self):
        while True:
            if l3.acquire():
                print("task3")
                l1.release()


if __name__ == '__main__':
    l1 = threading.Lock()
    l2 = threading.Lock()
    l2.acquire()
    l3 = threading.Lock()
    l3.acquire()

    t1 = My_thread_1()
    t2 = My_thread_2()
    t3 = My_thread_3()
    t1.start()
    t2.start()
    t3.start()
