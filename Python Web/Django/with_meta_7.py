# https://blog.csdn.net/dashoumeixi/article/details/80772832

class super_meta(type):  # 顶层元类 ，重定义__call__
    def __call__(self, *args, **kwargs):
        print('Super_meta __call__ :', self, args, kwargs)
        aClass = type.__call__(self, *args, **kwargs)  # 返回已经创建的类对象(并不是元类对象!!!)
        print('->>>>>Super_meta class 创建完成:', aClass)
        return aClass


# 还是一个元类, 元类本身还可以有元类,可元类并不会被实例化!!!
class sub_meta(type, metaclass=super_meta):
    def __new__(cls, *args, **kwargs):
        print('sub_meta __new__:', cls, args, kwargs)
        return type.__new__(cls, *args, **kwargs)  # 调用父类的__new__

    def __init__(self, *args, **kwargs):
        print('sub_meta __init__:', self, args, kwargs)


class Foo(metaclass=sub_meta):
    pass


Foo
