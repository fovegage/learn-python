class A(type):
    __instance = None

    def __call__(cls, *args, **kwargs):
        # 隐式的实现了  type()
        print(cls, args, kwargs)
        if not cls.__instance:
            cls.__instance = type.__call__(cls, *args, **kwargs)
        return cls.__instance


class B(metaclass=A):
    a = 1

B()
# b1 = B()
# b2 = B()
# print(b1, b2)
