# -*- coding: utf-8 -*-
# @Time    : 2018/12/18 16:44
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : super_Stu3.py
# @Software: PyCharm

# 重写
# __mro__ 查看类调用顺序
class A:
    def __init__(self, obj):
        self.obj = obj

    def __getattr__(self, item):
        """
        如果 查询不到
        :param item:
        :return:
        """
        return getattr(self.obj, item)

    def __setattr__(self, key, value):
        pass
        # if str(key).startswith('_'):
        #     super().__setattr__(key, value)
        # else:
        #     setattr(self.obj, key, value)


class B:
    def __getattr__(self, item):
        if item == 'age':
            return 25

    def __setattr__(self, key, value):
        super().__setattr__(key, value)


b = B()
print(b.age)
b.name = 'Gage'
print(b.__dict__)
