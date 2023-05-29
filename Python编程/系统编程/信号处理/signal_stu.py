# -*- coding: utf-8 -*-
# @Time    : 2018/11/22 16:52
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : signal_stu.py
# @Software: PyCharm

# USR1 用户自定义信号  windows不可使用
# 仅可以使用下面的几个信号，在windows
# SIGABRT
# SIGFPE
# SIGILL
# SIGINT
# SIGSEGV
# SIGTERM
import os
import signal
import time
import traceback


# 这两个参数Python解释器会自动传入，因此我们不必显示传入
def handle_SIGUSR1(signum, frame):
    print('handle sighup!{0}{1}'.format(os.linesep, '*' * 100))
    print(os.linesep.join(traceback.format_stack(frame)))  # 打印详细运行信息


def main():
    signal.signal(signal.SIGUSR1, handle_SIGUSR1)  # 注册SIGUSR1信号的处理器为handle_SIGUSR1函数
    print(signal.getsignal(signal.SIGUSR1))  # 获取SIGUSR1信号目前的处理器

    time.sleep(3)  # 或者使用signal.pause()
    os.kill(os.getpid(), signal.SIGUSR1)  # 向当前进程发送SIGUSR1信号
    time.sleep(3)

    print('done')


if __name__ == '__main__':
    main()
