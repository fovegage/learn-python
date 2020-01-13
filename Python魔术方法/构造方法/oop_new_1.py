class Foo:
    def __new__(cls, x):
        print(cls, 'new')
        # return super().__new__
        # 没有继承 只返回类
        return super(Foo, cls).__new__(cls)

    def __init__(self, x):
        self.x = x
        print(self, 'foo')


class Bar(Foo):
    def __init__(self, x):
        # 使用 super 变成了自己的
        super().__init__(x)
        print(self, 'bar')


Bar(5)
