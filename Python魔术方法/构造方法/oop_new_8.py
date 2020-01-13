class A(object):
    __instance = None

    def __call__(cls, *args, **kwargs):
        print(dir(cls))
        # 隐式的实现了  type()
        print(cls, args, kwargs)
        return 1
        # if not cls.__instance:
        #     cls.__instance = A.__call__(cls, *args, **kwargs)
        # return cls.__instance

    def add(self, x):
        print(x)


class B(A):
    a = 1


b = B()
print(b())
# b1 = B()
# b2 = B()
# print(b1, b2)
