# 参考链接
# http://www.simeonvisser.com/posts/python-3-using-yield-from-in-generators-part-2.html
# http://www.simeonvisser.com/posts/python-3-using-yield-from-in-generators-part-1.html
s = 'abc'
d = [1, 2, 3]


def chain1(*iterable):
    print(iterable)
    for item in iterable:
        for e in item:
            yield e


def chain2(*iterable):
    print(iterable)
    for item in iterable:
        yield from item


print(list(chain2(s, d)))

n = 1
if n:
    print(1)

from collections.abc import Generator, Iterator

print(isinstance((x for x in range(3)), Generator))

g = (x for x in range(3))

print(g)


def gen():
    item = 4
    if item > 3:
        yield item


print('#' * 100)


def generator():
    while True:
        receive = yield 1
        print('extra' + str(receive))


g = generator()
# print(next(g))
g.send(None)
print(g.send(111))
# print(next(g))
