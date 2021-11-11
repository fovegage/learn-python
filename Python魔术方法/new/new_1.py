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

    def __init__(self, x=None):
        print(f"{self} --- > init")
        self.x = x

    @staticmethod
    def test_static():
        print(1)

    @classmethod
    def test_class(cls):
        print(cls)


if __name__ == '__main__':
    """
    __init__ 为构造方法  无需返回值
    __new__  类函数  该函数将初始化  __init__ 中传入的参数  注意只在类实例化的时候 在魔术方法才被调用  负责类的初始化
    """
    SinglePar.test_class()
    # s1 = SinglePar(1)
    # s2 = SinglePar(2)
    #
    # print(s1)
    # print(s2)
