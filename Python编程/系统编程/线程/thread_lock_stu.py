# -*- coding: utf-8 -*-
# @Author: fovegage
# @File: thread_lock_stu.py
# @Email: fovegage@gmail.com
# @Date: 2018-09-21 16:41:02
# @Last Modified time: 2018-09-21 16:41:07

import threading

# 可以加锁  也可以延时
num = 0
class My_Thread_1(threading.Thread):
    def run(self):
        global num
        for i in range(1000000):
            flag = mutex.acquire(True)
            if flag:
                num += 1
                mutex.release()
        print("线程1：{}".format(num))

class My_thread_2(threading.Thread):
    def run(self):
        global num
        for i in range(1000000):
            flag = mutex.acquire(True)
            if flag:
                num += 1
                mutex.release()
        print("线程2：{}".format(num))


if __name__ == '__main__':
    mutex = threading.Lock()
    # mutex.acquire()
    t1 = My_Thread_1()
    t1.start()
    t2 = My_thread_2()
    t2.start()
