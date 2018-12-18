# -*- coding: utf-8 -*-
# @Time    : 2018/11/14 14:04
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : with协议.py
# @Software: PyCharm

# 自己实现的上下文管理器
class Close():
    def __init__(self, obj):
        self.obj = obj

    def __enter__(self):
        return self.obj  # 返回作为as目标

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            self.obj.close()
        except AttributeError:
            print(exc_type)


# 这是我们自定义的  上下文管理器    它自带close() 功能
with Close(int(5)) as i:
    i += 1
    print(i)

