# -*- coding: utf-8 -*-
# @Time    : 2018/12/27 18:24
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 删除.py
# @Software: PyCharm

# 指定集合删除
set1 = {'a', 'b', 'c'}
set2 = {'b'}
set1.difference_update(set2)
print(set1)

# 指定元素删除
set1.discard('c')
# set1.remove('c')  # 效果一样
print(set1)

# 清空
set1.clear()
print(set1)

# 随机删除  由于集合存储是随机的
set1.pop()