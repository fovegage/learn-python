# -*- coding: utf-8 -*-
# @Author: fovegage
# @File: thread_stu.py
# @Email: fovegage@gmail.com
# @Date: 2018-09-21 15:46:09
# @Last Modified time: 2018-09-21 16:39:39


import os
# 线程是在进程中开启的
# 对比for循环，他可以一次执行完成
import threading
from time import sleep


def sorry(i):
    print('say sorry  {}'.format(i))
    sleep(1)


if __name__ == '__main__':
    for i in range(1, 10):
        t = threading.Thread(target=sorry, args=(i,))
        t.start()


# 主线程会等待所有线程执行结束后停止

def sing():
    for x in range(3):
        print('eating {}'.format(x))
        sleep(1)


def dance():
    for i in range(3):
        print('dancing {}'.format(i))
        sleep(1)


if __name__ == '__main__':
    print("主进程{}开始执行".format(os.getpid()))
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)

    t1.start()
    t2.start()

    # 延时是操作系统堵塞运行，具体取决于操作系统调度
    sleep(6)
    print('主进程执行结束')


# 线程的执行顺序
# 同时进行，线程继承
class MyThread(threading.Thread):
    def run(self):
        for x in range(1, 6):
            sleep(1)
            print(self.name + "@{}".format(x))


if __name__ == '__main__':
    for x in range(1, 3):
        t = MyThread()
        t.start()
