import os
from collections import deque


# print(os.path.join(os.path.dirname(__file__), 'file', 'd'))
# https://blog.csdn.net/lanchunhui/article/details/51581540

def search(f, p, d=5):
    # 声明一个队列，长度为d
    save = deque(maxlen=d)
    # 文件对象f当作迭代对象，系统将自动处理IO缓存和内存管理
    for line in f:
        if p in line:
            yield line, save
        save.append(line)


def test():
    with open('./file/a.txt') as f:
        for line, save in search(f, 'python', 5):
            print(line, end='')


if __name__ == '__main__':
    with open('./file/a.txt') as f:
        while True:
            line = f.readline()
            print(line, end='')
            if not line:
                break

from collections import defaultdict