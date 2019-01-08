# -*- coding: utf-8 -*-
# @Time    : 2019/1/7 15:50
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 皆对象.py
# @Software: PyCharm

age = 25
print(age.__class__.__class__)

# 1）Foo中有__metaclass__这个属性吗？如果是，Python会在内存中通过__metaclass__创建一个名字为Foo的类对象（我说的是类对象，请紧跟我的思路）。
# 2）如果Python没有找到__metaclass__，它会继续在父类中寻找__metaclass__属性，并尝试做和前面同样的操作。
# 3）如果Python在任何父类中都找不到__metaclass__，它就会在模块层次中去寻找__metaclass__，并尝试做同样的操作。
# 4）如果还是找不到__metaclass__,Python就会用内置的type来创建这个类对象。