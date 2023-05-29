# -*- coding: utf-8 -*-
# @Author: fovegage
# @File: thread_global_stu.py
# @Email: fovegage@gmail.com
# @Date: 2018-09-21 16:28:08
# @Last Modified time: 2018-09-21 16:38:40

# 与进程相比较，线程的全局变量可以共享

import threading

num = 100


class My_Thread_1(threading.Thread):
    def run(self):
        global num
        for x in range(3):
            num = num + 1

        print(num)


class My_Thread_2(threading.Thread):
    def run(self):
        global num
        print(num)


if __name__ == '__main__':
    t1 = My_Thread_1()
    t2 = My_Thread_2()

    t1.start()
    t2.start()

# 即使不使用global 数据也是共享的
