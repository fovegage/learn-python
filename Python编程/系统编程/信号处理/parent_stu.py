# -*- coding: utf-8 -*-
# @Time    : 2018/11/22 17:22
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : parent_stu.py
# @Software: PyCharm
import os
import signal


def SIGCHLD_handle():
    print(
        '执行---SIGCHLD，在一个进程终止或者停止时，将SIGCHLD信号发送给其父进程，按系统默认将忽略此信号，如果父进程希望被告知其子系统的这种状态，则应捕捉此信号。')


def main():
    signal.signal(signal.SIGCHLD, SIGCHLD_handle)
    pid = os.fork()
    if pid == 0:
        print('child')
    else:
        print('parent')
        os.wait()  # Wait for completion of a child process
    print('done')


#  先执行 parent
if __name__ == '__main__':
    main()

# parent
# child
# done
# 执行---SIGCHLD，在一个进程终止或者停止时，将SIGCHLD信号发送给其父进程，按系统默认将忽略此信号，如果父进程希望被告知其子系统的这种状态，则应捕捉此信号。
# done
