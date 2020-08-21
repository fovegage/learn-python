"""
必须返回实例对象
在new进行实例化
"""

import dis


class A:
    a = 1

    def __new__(cls, *args, **kwargs):
        print(cls)
        # 会造成无限递归
        # return cls()
        return super().__new__(cls)

    def __init__(self, x):
        print(self)
        self.x = x


# print(dis.dis(A))
a = A(5)
print(a.x)
