def with_metaclass(meta, *base):
    # print(meta)
    # meta 是type 的子类
    return meta('tmp_class', base, {})


class meta():
    def __new__(cls, *args, **kwargs):
        return super(meta, cls).__new__(cls, *args, **kwargs)


class test_meta(metaclass=meta):
    """
    使用 __new__ 阻截
    """

    def __new__(cls, name, bases, d):
        # print(cls, name, bases, d, 'test')
        d['a'] = 'hello'
        return type.__new__(cls, name, bases, d)


class Foo(test_meta):
    pass


print(Foo.__mro__)
