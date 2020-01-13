# (a, b)  (*args)
#

# *args = a, b, c
# https://blog.csdn.net/chenjinyu_tang/article/details/8136841
# 如果函数调用 传递 *args 则 函数必须用相应的变量来接收 h1() h2()
def h1(args):
    print(args)


def h2(args):
    print(*args)


# 函数中的 *args 用来接收对应的变量
def h3(*args):
    print(args)


def h4(*args):
    print(*args)


def hello(args):
    print(args)