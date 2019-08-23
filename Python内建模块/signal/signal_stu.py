# -*- coding: utf-8 -*-
# @Time    : 2018/11/21 16:39
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : signal_stu.py
# @Software: PyCharm


# !/usr/bin/env python3
# coding=utf-8

import time
import signal


def handle_SIGALRM(signum, frame):
    print('alarm {0}!'.format(int(time.time())))


def main():
    signal.signal(signal.SIGALRM, handle_SIGALRM)  # 注册SIGALRM信号的处理器为handle_SIGALRM函数

    signal.alarm(3)  # 设置每3秒发送一次SIGALRM信号
    time.sleep(10)  # 某些耗时的操作
    signal.alarm(0)  # 取消定时发送SIGALRM信号

    print('done')


if __name__ == '__main__':
    main()
