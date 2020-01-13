class A(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            # cls.__instance = super(A, cls).__new__  # built-in method
            cls.__instance = super(A, cls).__new__(cls, *args, **kwargs)
        return cls.__instance


class B(A):
    a = 1


b1 = B()
b2 = B()
print(b1, b2)


class C:
    a = 2

# c1 = C()
# c2 = C()

# print(c1, c2)
