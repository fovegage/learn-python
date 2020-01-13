# https://www.jb51.net/article/113154.htm


def cusomer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('cus{}'.format(n))
        r = '200'


def producer(c):
    # 起动
    c.send(None)
    n = 0
    while n < 5:
        n += 1
        print('pro{}'.format(n))
        r = c.send(n)
        print('return{}'.format(r))

    c.close()


c = cusomer()
producer(c)
