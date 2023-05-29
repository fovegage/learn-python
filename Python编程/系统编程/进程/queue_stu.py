# -*- coding: utf-8 -*-
# @Time    : 2018/9/20 17:55
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : queue_stu.py
# @Software: PyCharm

from multiprocessing import Queue, Process


def write(q):
    info = ["A", "B", "C"]
    for i in info:
        print("发送{}.".format(i))
        q.put(i)


def read(q):
    while True:
        if not q.empty():
            info = q.get(True)
            print("得到{}.".format(info))
        else:
            break


if __name__ == '__main__':
    q = Queue()

    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pw.join()
    pr.start()
    pr.join()
