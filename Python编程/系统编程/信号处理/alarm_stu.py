# -*- coding: utf-8 -*-
# @Time    : 2018/11/22 17:42
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : alarm_stu.py
# @Software: PyCharm

# !/usr/bin/env python3
# coding=utf-8

import time
import signal


def handle_SIGALRM(signum, frame):
    print('alarm {0}!'.format(int(time.time())))


def main():
    signal.signal(signal.SIGALRM, handle_SIGALRM)

    signal.alarm(3)  # 三秒发送一次
    time.sleep(10)  # 会不执行  可用于判断是否超时
    signal.alarm(0)  # 取消发送信号

    print('done')


if __name__ == '__main__':
    main()

# alarm 1230747556!
# done