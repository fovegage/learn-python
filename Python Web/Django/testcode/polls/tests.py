# from django.test import TestCase


# Create your tests here.

# class Model(dict):
#     # 继承dict原理
#     def __init__(self, **kwargs):
#         print(kwargs)
#         super().__init__(**kwargs)
#
#
# m = Model(name="Gage")
#
#
# print(dict(name="gage"))


# class Person:
#     def __init__(self, max_length=None):
#         print(self)
#         self.max_length = max_length
#
#     def check(self, **kwargs):
#         errors = []
#         print(errors)
#         return errors
#
#
# class Son(Person):
#     def __init__(self, **kwargs):
#         print(self)
#         super().__init__(**kwargs)
#
#     def check(self, **kwargs):
#         errors = super().check(**kwargs)
#         print(self._check_length())
#         errors.append(self._check_length(**kwargs))
#         print(errors)
#         return errors
#
#     def _check_length(self, **kwargs):
#         if self.max_length is None:
#             return 1
#             # return "max_length field must exist"
#
#         if self.max_length < 5:
#             return 2
#             # return "max length must lte 5"
#
#
# s = Son(max_length=6)
# s.check()
# print(s.__dict__)

import itchat

itchat.auto_login()

itchat.send('Hello, filehelper', toUserName='filehelper')
