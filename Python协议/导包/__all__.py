# -*- coding: utf-8 -*-
# @Time    : 2019/4/8 11:38
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : __all__.py
# @Software: PyCharm

__all__ = ['name', 'num', 'age']
num = 1
name = "Gage"

def age():
    return 25

# 需要注意的是 __all__ 只影响到了 from <module> import * 这种导入方式， 即如果 age 不在 __all__ 里面 即会报异常
# The following will trigger an exception, as "age" is not exported by the module


# 对于 from <module> import <member> 导入方式并没有影响，仍然可以从外部导入。