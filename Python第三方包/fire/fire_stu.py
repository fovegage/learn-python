# -*- coding: utf-8 -*-
# @Time    : 2018/11/19 14:24
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : fire_stu.py
# @Software: PyCharm
import fire

class Calculator(object):
  """A simple calculator class."""

  def double(self, number):
    return 2 * number

if __name__ == '__main__':
  fire.Fire(Calculator)