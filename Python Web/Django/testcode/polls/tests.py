from django.test import TestCase


# Create your tests here.

class Model(dict):
    # 继承dict原理
    def __init__(self, **kwargs):
        print(kwargs)
        super().__init__(**kwargs)


m = Model(name="Gage")


print(dict(name="gage"))
