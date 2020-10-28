# -*- coding: utf-8 -*-
# @Time    : 2018/12/18 16:40
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : abc_stu.py
# @Software: PyCharm
import abc
import six


# 类内 class 如何调用  研究Django Meta的实现
# abc.
@six.add_metaclass(abc.ABCMeta)  # 声明后子类必须实现  不然会报错
class BaseClass:
    @abc.abstractmethod
    def fun_a(self):
        """
        implement
        """


class ImplClass(BaseClass):
    def fun_a(self):
        print("I'm implemented")


impl = ImplClass()
impl.fun_a()
