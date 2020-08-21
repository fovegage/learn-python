"""
单列模式
__new__ 关键 return 回去 class
"""


class SinglePar:
    __instance = None

    def __new__(cls, *args, **kwargs):
        print(cls, args)
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        print(f"{cls.__instance} ---> instance")
        return cls.__instance

    def __init__(self, x):
        print(f"{self} --- > init")
        self.x = x


s1 = SinglePar(1)
s2 = SinglePar(2)

print(s1)
print(s2)
