# -*- coding: utf-8 -*-
# @Time    : 2019/4/9 9:35
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : std_stu.py
# @Software: PyCharm
import sys

'buffer', 'close', 'closed', 'detach', 'encoding', 'errors', 'fileno', 'flush', \
'isatty', 'line_buffering', 'mode', 'name', 'newlines', 'read', 'readable', 'readline', \
'readlines', 'seek', 'seekable', 'tell', 'truncate', 'writable', 'write', 'writelines'

# 标准输出
sys.stdout.write('hello' + '\n')
sys.stdout.flush()  # 缓冲

# 用户输入
print('Plase input your name: ')
name = sys.stdin.readline()[:-1]
print(name)


# 打印错误信息为 红色
sys.stderr.write('hello')