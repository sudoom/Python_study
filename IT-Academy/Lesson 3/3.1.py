a = [5, 2, 3, 1, 4]
b = a[:]
b.sort()
a.remove(b[-1])
print(a)
