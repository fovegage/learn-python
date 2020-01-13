class metacls(type):
    def __new__(cls, name, bases, attrs):
        print(cls, name, bases, attrs)
        attrs['name'] = 'the5fire'
        return type.__new__(cls, name, bases, attrs)


class Foo(metaclass=metacls):
    pass
    # __metaclass__ = metacls


Foo()
