from collections import defaultdict

# value 用 list
d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
print(d)

# 去重
d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['a'].add(2)
print(d)

d1 = {}
d1.setdefault('a', []).append(1)
print(d1)

d2 = {}.fromkeys(['a'], 0)
print(d2)

d3 = {}.fromkeys({'a': 0})
print(d3)

lt = ['a', 'b', 'b']
d4 = defaultdict(list)
for key, value in enumerate(lt):
    d4[value].append(key)

print(d4)