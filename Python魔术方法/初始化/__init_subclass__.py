# -*- coding: utf-8 -*-
# @Time    : 2019/3/25 11:01
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : __init_subclass__.py
# @Software: PyCharm

class Person(object):

    def __init__(self):
        pass

    def __init_subclass__(cls, **kwargs):
        rn.set_name(cls)

    @classmethod
    def name(cls):
        raise NotImplementedError



class RegisterName(object):

    def __init__(self):
        self._info = {}

    def set_name(self, classnmae: Person):
        name = classnmae.name()
        self._info[name] = classnmae
        return True

    def get_value(self):
        return self._info


rn = RegisterName()


class XiaoHong(Person):
    @classmethod
    def name(cls):
        return 'XiaoHong'


xh = XiaoHong()
print(rn.get_value())