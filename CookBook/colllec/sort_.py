l = {'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.2, 'FB': 10.75}

# print(min(zip(l.values(), l.keys())))
# print(sorted(zip(l.values(), l.keys())))

z = zip(l.values(), l.keys())
print(list(z))
print(list(z))