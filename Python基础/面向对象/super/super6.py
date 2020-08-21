class A:
    def __init__(self):
        print(f"{self} --- A")


class B(A):
    def __init__(self):
        print(f"{self} --- B")


class C(A):
    def __init__(self):
        print(f"{self} --- C")


class D(B, C):
    def __init__(self):
        print(f"{self} --- D")
        super().__init__()


d = D()
print(D.__mro__)