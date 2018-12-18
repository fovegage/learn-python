# -*- coding: utf-8 -*-
# @Time    : 2018/11/23 11:12
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 无参数.py
# @Software: PyCharm

# 装饰器即验证函数
# 无参数
def makeBold(fun):  #  接受函数
    def wrapped():  # 接受参数
        return "<b>" + fun() + "</b>"  # 第一步 返出 验证
    return wrapped  # 将内部函数返出

@makeBold
def test1():
    return "hello world-1"

print(test1())