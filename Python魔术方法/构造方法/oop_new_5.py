class A(type):
    __instance = None

    def __new__(cls, name, base, d):
        # 隐式的实现了  type()
        print(cls, name)
        if not cls.__instance:
            cls.__instance = type.__new__(cls, name, base, d)
        return cls.__instance


class B(metaclass=A):
    a = 1


b1 = B()
b2 = B()
print(b1, b2)
