#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File:isPalindrome.py 
@Author:fovegage
@Contact:fovegage@gmail.com
@Created Time:2019/8/21 13:04   
@Version:1.0
'''


# 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if str(x)[::-1] == str(x):
            return True
        else:
            return False


s = Solution()
print(s.isPalindrome(-121))
