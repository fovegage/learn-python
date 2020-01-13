# __new__  在 super 和 type 的调用是有区别的


class Person:
    def __new__(cls, *args, **kwargs):
        print(cls, args, kwargs)
        return super().__new__(cls)

    def __init__(self, a):
        self.a = a

    def print(self):
        print('hello')


p = Person(1)
print(p.a)
