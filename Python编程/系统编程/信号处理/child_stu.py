# -*- coding: utf-8 -*-
# @Time    : 2018/11/22 17:11
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : child_stu.py
# @Software: PyCharm

# signal 不可定义在子进程

# 当handler为signal.SIG_DFL时，表示接收信号后，程序按系统默认行为执行；
# 当handler为signal.SIG_IGN时，则表示接收信号后，程序忽略该信号，继续自身运行。
import signal
from threading import Thread


def child():
    signal.signal(signal.SIGUSR1, signal.SIG_IGN)
    print('child thread')


def main():
    thread = Thread(target=child)
    thread.start()
    thread.join()
    print('done')


if __name__ == '__main__':
    main()
