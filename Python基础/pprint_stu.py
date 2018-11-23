# -*- coding: utf-8 -*-
# @Time    : 2018/11/22 16:25
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : pprint_stu.py
# @Software: PyCharm

import pprint

data = (
    "this is a string", [1, 2, 3, 4], ("more tuples",
                                       1.0, 2.3, 4.5), "this is yet another string"
)

pprint.pprint(data)   # 格式化打印
print('-'*30)
print(data)