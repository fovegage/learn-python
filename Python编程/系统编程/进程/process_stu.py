# -*- coding: utf-8 -*-
# @Time    : 2018/9/20 11:15
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : process_stu.py
# @Software: PyCharm

import os
import time
from multiprocessing import Process


class Process_class(Process):
    def __init__(self, push):
        Process.__init__(self)
        self.push = push

    def run(self):
        print("子进程{}开始执行,父进程为{}.".format(os.getpid(), os.getppid()))
        start = time.time()
        time.sleep(self.push)
        stop = time.time()
        print("子进程结束,耗时{}s.".format(stop - start))


if __name__ == '__main__':
    print("当前程序{}开始执行.".format(os.getpid()))
    start = time.time()
    p = Process_class(2)
    p.start()
    p.join()
    stop = time.time()
    print("当前进程{}执行结束.".format(os.getpid()))

# 执行结果
"""
当前程序20796开始执行.
子进程34652开始执行,父进程为20796.
子进程结束,耗时2.000720500946045s.
当前进程20796执行结束.
"""
