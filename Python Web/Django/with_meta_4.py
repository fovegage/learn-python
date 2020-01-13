class Upper(type):
    def __new__(cls, classname, baseclass, attrs):
        print(classname, baseclass, attrs)
        attrs_ = {key.upper(): value for key, value in attrs.items() if not key.startswith('__')}
        return type(classname, baseclass, attrs_)


class Foo(metaclass=Upper):
    bar = 1


Foo()
