# -*- coding: utf-8 -*-
# @Time    : 2018/12/29 17:16
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : compile_stu.py
# @Software: PyCharm

# compile()  编译字符代码  必须借助于 exec() 和 eval()

str = "for i in range(5): print(i)"
print(compile(str, '<int>', 'exec'))
exec(compile(str, '', 'exec'))