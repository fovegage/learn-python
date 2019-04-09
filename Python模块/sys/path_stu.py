# -*- coding: utf-8 -*-
# @Time    : 2019/4/9 9:43
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : path_stu.py
# @Software: PyCharm

# 获取指定模块搜索路径的字符串集合，可以将写好的模块放在得到的某个路径下，就可以在程序中import时正确找到
import sys

print(sys.path)
# sys.path 返回列表 我们可以把想要添加的 自定义模块 append 到 list 中

# sys.path.append("自定义模块路径")