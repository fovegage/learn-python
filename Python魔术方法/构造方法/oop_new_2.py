class A:
    def __init__(self):
        print(self)
        self.n = 2

    def add(self, m):
        self.n += m


class B(A):
    def __init__(self):
        print(self)
        super().__init__()
        self.n = 3

    def add(self, m):
        super().add(m)
        self.n += 3


b = B()
b.add(2)
print(b.n)


class C(A):
    def __init__(self):
        self.n = 4

    def add(self, m):
        print('self is {0} @C.add'.format(self))
        super().add(m)
        self.n += 4


class D(B, C):
    def __init__(self):
        self.n = 5

    def add(self, m):
        print('self is {0} @D.add'.format(self))
        super().add(m)
        self.n += 5


d = D()
d.add(2)
print(d.n)

print(D.__mro__)