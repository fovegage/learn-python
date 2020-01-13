# https://blog.csdn.net/liuchunming033/article/details/48498061

# 需要使用 super 等方式手动 覆写 父类的构造方法
class A:
    def __init__(self):
        print(self, A)
        # print(isinstance(A, self))


A()

