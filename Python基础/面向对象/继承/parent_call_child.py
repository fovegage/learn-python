class A(type):
    def __new__(cls, name, base, attr):
        print(cls, name, base, attr)
        return type.__new__(cls, name, base, attr)
    # def __init__(self, **kwargs):
    #     print(self)
    #     pass


class B(metaclass=A):
    def __init__(self, **kwargs):
        # print(super().__init__(**kwargs))
        # print(super().__init__)
        super().__init__()


class P(B):
    pass


P()
