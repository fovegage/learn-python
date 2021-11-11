import threading
from queue import Queue

q = Queue(10)

"""
https://www.liujiangblog.com/course/python/80
"""
def producer(i):
    """
    不断的生产
    """
    while True:
        q.put(f'厨师{i}在做饭')


def consumer(i):
    """
    顾客消费
    """
    while True:
        print(f'顾客{i}正在吃 {q.get()}')


for p in range(3):
    t1 = threading.Thread(target=producer, args=(p,))
    t1.start()

for c in range(10):
    t2 = threading.Thread(target=consumer, args=(c,))
    t2.start()
