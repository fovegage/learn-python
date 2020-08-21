def dupli(items, key=None):
    """
    用 key 过滤 重复元素 yield 返回过滤的值
    该方法和 sorted 中的 key 类似
    :param items:
    :param key:
    :return:
    """
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)



{}.update()


items = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
print(list(dupli(items, key=lambda x: (x['x'], x['y']))))


sorted(items, key=lambda x: (x['x'], x['y']))
print(items)