# 类执行过程
# 必须实例化，类才可以执行，及调用call
# 实例化是调用的__call__ 方法
# 1、执行 __prepare__
# 2、执行类语句
# 3、__new__
# 4、__init__
# 5、__call__

class Foo:
    def __new__(cls, *args, **kwargs):
        print(cls, args, kwargs)
        return type('p', (), {})

    a = 1


class Foo1(type):
    def __new__(cls, name, base, d):
        print(cls, name)
        return type.__new__(cls, name, base, d)

    a = 1


class Person(Foo):
    bar = 1


# 普通继承不实例化不会进行 call 即__call__
Person
# Person()

# class 创建过程
# class Bar:
#     pass
#
#
# f = type('Foo', (Bar,), {})
#
# print(f())
