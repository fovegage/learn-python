class A:
    def __init__(self):
        print(f"{self} --- A")


class B:
    def __init__(self, b):
        self.b = b
        print(f"{self} --- B")


class C(A, B):
    def __init__(self):
        print(__class__)
        print(f"{self} --- C")
        super().__init__()


c = C()
print(C.__mro__)