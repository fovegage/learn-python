# -*- coding: utf-8 -*-
# @Time    : 2019/3/22 17:47
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : __set_name__.py
# @Software: PyCharm

# 在创建拥有类所有者时调用，描述符已分配给name。
class Philosopher:
    # 当被继承时调用 不继承不会调用
    def __init_subclass__(cls, default_name, **kwargs):
        # super().__init_subclass__(**kwargs)
        print(f"Called __init_subclass({cls}, {default_name})")
        cls.default_name = default_name

class AustralianPhilosopher(Philosopher, default_name="Bruce"):
    pass

class GermanPhilosopher(Philosopher, default_name='Gage'):
    default_name = "Hegel"
    print("Set name to Hegel")

Bruce = AustralianPhilosopher()
Mistery = GermanPhilosopher()
print(Bruce.default_name)
print(Mistery.default_name)