# -*- coding: utf-8 -*-
# @Time    : 2018/11/22 17:49
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : traceback_stu.py
# @Software: PyCharm

import traceback

def func(a, b):
	return a / b

if __name__ == '__main__':
	import sys
	import traceback
	try:
		func(1, 0)
	except Exception as e:
		print("print exc")
		traceback.print_exc(file=sys.stdout)
