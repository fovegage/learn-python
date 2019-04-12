# -*- coding: utf-8 -*-
# @Time    : 2018/12/21 18:17
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : bisect_stu.py
# @Software: PyCharm

import bisect


data = [2, 1, 9, 7]
data.sort()

# 共用内存地址在 左边插入
bisect.insort(data, 5)
print(data)

# 查找该数值将会插入的位置并返回，而不会插入
index = bisect.bisect(data, 99)
print(index)

# 如果插入的数据在数组中，选择右插入还是左插入
# bisect.bisect_right()
# bisect.insort_right()