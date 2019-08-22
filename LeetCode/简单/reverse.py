#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File:reverse.py 
@Author:fovegage
@Contact:fovegage@gmail.com
@Created Time:2019/8/21 11:22   
@Version:1.0
'''

"""
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
"""


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x < 0:
            x = -int(str(x)[1:][::-1])
        else:
            x = int(str(x)[::-1])

        if -2 ** 31 > x or x > 2 ** 31 - 1:
            return 0
        else:
            return x


s = Solution()
print(s.reverse(1534236469))

print(2 ** 31 - 1)
