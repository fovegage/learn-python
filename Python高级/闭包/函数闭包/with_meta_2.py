def with_metaclass(meta, *base):
    # print(meta)
    # meta 是type 的子类
    # 中间方法
    print(meta)
    # 这里利用元类创建类
    return meta('tmp_class', base, {})


class test_meta(type):
    """
    使用 __new__ 阻截
    """

    def __new__(cls, name, bases, d):
        print(cls, name, bases, d)
        d['a'] = 'hello'
        # 顶级元类 是等效的
        return type(name, bases, d)
        return type.__new__(cls, name, bases, d)


# class Foo(with_metaclass(test_meta)):
#     pass
#
#
# print(Foo.__mro__)

a = with_metaclass(test_meta)

print(a)
