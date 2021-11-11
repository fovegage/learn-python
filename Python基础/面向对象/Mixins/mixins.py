"""
drf mixins
"""

from collections import defaultdict


class CheckKeyMixin:
    __slots__ = ()

    def __setitem__(self, key, value):
        print(self, key, value)
        if key in self:
            raise KeyError(f'{key} is exist')
        return super().__setitem__(key, value)


class Person(dict):
    pass


class Man(CheckKeyMixin, defaultdict):
    pass


if __name__ == '__main__':
    """
    __setattr__
    __setitem__
    from rest_framework.mixins import CreateModelMixin
    mixin 只扩展功能 无构造
    drf 这里其实对 方法进行重写了  这也是一种设计模式
    """
    # 这里 之所以可以传值 是因为 dict 有构造
    man = Man(list)

    man['sex'].append(2)
    man['sex'] = "1"
