# -*- coding: utf-8 -*-
# @Time    : 2018/12/13 13:39
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : word.py
# @Software: PyCharm

class And(int):
    def __add__(self, other):
        return super(And, self).__add__(other)

a = And()

class Word(str):

    def __new__(cls, word):
        # 注意我们必须要用到__new__方法，因为str是不可变类型
        # 所以我们必须在创建的时候将它初始化
        if ' ' in word:
            print("Value contains spaces. Truncating to first space.")
            word = word[:word.index(' ')] #单词是第一个空格之前的所有字符
        return str.__new__(cls, word)

    def __gt__(self, other):
        return len(self) > len(other)
    def __lt__(self, other):
        return len(self) < len(other)
    def __ge__(self, other):
        return len(self) >= len(other)
    def __le__(self, other):
        return len(self) <= len(other)


print(Word('bar') == Word('bar'))

w = Word('hello')
print(w.__le__('yesyes'))