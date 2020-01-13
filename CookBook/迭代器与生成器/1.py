# 可以不用捕获异常 next(f, None) 指定None  
#   Return the next item from the iterator. If default is given and the iterator
#     is exhausted, it is returned instead of raising StopIteration.


with open('E:\\test.txt') as f:
    while True:
        line = next(f, None)
        if line is None:
            break
        print(line, end='')
