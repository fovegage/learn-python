class Upper(type):
    def __new__(cls, classname, baseclass, attrs):
        print(classname, baseclass, attrs)
        attrs_ = {key.upper(): value for key, value in attrs.items() if not key.startswith('__')}
        return type.__new__(cls, classname, baseclass, attrs_)
        return type(classname, baseclass, attrs_)


class Parent:
    def __init__(self):
        self.name = 1


class Foo(Parent, metaclass=Upper):
    bar = 1


print(Foo.__dict__)
