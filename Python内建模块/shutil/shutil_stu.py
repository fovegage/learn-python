# -*- coding: utf-8 -*-
# @Time    : 2019/4/9 17:13
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : shutil_stu.py
# @Software: PyCharm

import shutil

# 拷贝文件
shutil.copyfileobj(open('f:\\test.txt', 'r'), open('f:\\test1.txt', 'w'))

# 不需要使用 open
shutil.copyfile('f:\\test.txt', 'b.txt')

# 复制目录下的内容 若 dst 存在， 则报错
shutil.copytree('F:\\test\\a', 'F:\\test\\c')


# 删除文件目录  不管是不是为空
# shutil.rmtree('F:\\test\\test')
