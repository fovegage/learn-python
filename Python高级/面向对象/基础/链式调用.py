# -*- coding: utf-8 -*-
# @Time    : 2018/10/26 9:44
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 链式调用.py
# @Software: PyCharm

# 类链式调用
class Person:
    def name(self, name):
        self.name = name
        return self

    def age(self, age):
        self.age = age
        return self

    def show(self):
        print("My name is", self.name, "and I am", self.age, "years old.")



p = Person()
# p.name("Li Lei").age(15).show()  按顺序进行调用  调完name  调age
p.name('Gage')
p.age(25)
p.show()

# 方法链式调用
def sum(a, b):
    return a + b

def mul(a, b):
    return a * b

flag = False

# mul 函数名  mul() 执行函数
print((sum if flag else mul)(2, 4))  #三目运算


