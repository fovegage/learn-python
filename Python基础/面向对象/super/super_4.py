class A:
    def __init__(self):
        print(f"{self} --- A")
        pass


class B(A):
    def __init__(self):
        print(f"{self} --- B")
        super().__init__()


class C(B):
    def __init__(self):
        # C __mro__
        super().__init__()
        print(f"{self} --- C")



c = C()
print(C.mro())