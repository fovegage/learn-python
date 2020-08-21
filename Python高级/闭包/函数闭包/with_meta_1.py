def with_metaclass(meta, *base):
    return meta('tmp_class', base, {})


def with_metaclass1(meta, *base):
    """
    继承于 test_meta  但是却看不到test_meta

    :param meta:
    :param base:
    :return:
    """

    # print(meta, base, 'start')

    class metaclass(meta):
        """
        cls: 当前要创建类的名字
        name: 类的名字
        this_base 继承的类
        d 方法属性构成的字典
        """

        def __new__(cls, name, this_base, d):
            #
            # print(this_base[0].__class__)
            print(cls, name, this_base, d, 'with')
            # 注意这儿的返回  是base 继承的类  而不是this_base
            # 这一步就抛弃了 this_base class '__main__.temp_class'
            return meta(name, base, d)  # 完成实例化，并继承

        # @classmethod
        # def __prepare__(mcs, name, bases):
        #     pass

    # print('#' * 10)
    # print(type.__new__(metaclass, 'temp_class', (), {}).__mro__)
    # metaclass 的元类是test_meta
    # class 是 meatclass 的实例
    # object 是 class 的实例
    return type.__new__(metaclass, 'temp_class', (), {})  # 抛弃 返回 只有类继承才会调用，仅仅方法调用调用不会触发，因为方法不需要实例化


class test_meta_base(type):
    """
    使用 __new__ 阻截
    常常作为基类
    """

    # 该__new__ 绑定在 返回的 with_meta_class 中
    def __new__(cls, name, bases, d):
        print(cls, name, bases, d, 'base')
        d['a'] = 'hello'
        return type.__new__(cls, name, bases, d)


class Bar:
    a = 3


# 注意这里返回的是闭包内  类内存对象的地址
# 接着Foo可以继承
# 在Python继承创建过程中， 是靠寻找 metaclass 这个属性来进行类创建的
# 如果在多层继承中为发现metaclass 将使用底层的type进行创建
# 该类必须继承显式的继承 type
# ex = with_metaclass1(test_meta_base)
#
# print('#' * 10)
# print(ex)


# with_metaclass1(test_meta_base) 返回的是一个类
# 使用 Foo 继承
# class Foo(with_metaclass1(test_meta_base)):
class Foo(metaclass=test_meta_base):
    bar = '1'
    """
    使用 with_metaclass 关联 Foo 和 base
    """
    pass

# 注意这里子类可以调用父类
# print(Foo.a)
# print(Foo.__mro__)
# print(Foo.__dict__)
