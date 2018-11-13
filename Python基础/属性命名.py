# -*- coding: utf-8 -*-
# @Time    : 2018/11/13 10:21
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 属性命名.py
# @Software: PyCharm

# __ 一般放在父类，避免与子类属性名冲突  无法在外界直接访问
#  _ 和 __ 在类内可以表使用
class Person():
    def __init__(self, name, age, length):
        self.name = name
        self._age = age
        self.__length = length

    def print(self):
        print(self.name)
        print(self._age)
        print(self.__length)

    def dowork(self):
        self._work()
        self.__sing()

    def _work(self):
        print(self.name + '在工作')

    def __sing(self):
        print(self.name + '在唱歌')


class Student(Person):
    # def info(self, name, age, length):
    #     self.name = name
    #     self._age = age
    #     self.__length = length

    def student_print(self):
        print(self.name)
        print(self._age)
        # print(self.__length)

    @staticmethod
    def testBug():
        _Bug.showBug()

# _ 子类可以访问  但是不允许导入
class _Bug():
    @staticmethod
    def showBug():
        print('bug')


# p = Person('Gage', 25, 180)
# p.print()
# p.dowork()

s = Student('Gage', 25, 'hello')
# s.student_print()   # 子类不可以访问 __ 属性，父类独有  可以访问 _ 属性
s.print()
s.testBug()