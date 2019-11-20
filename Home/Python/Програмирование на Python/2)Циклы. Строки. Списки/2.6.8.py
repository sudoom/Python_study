x = int(input())
t, a = list(), list()
for i in range(1, x+1):
    t.append([i]*i)
for i in t:
    a.extend(i)
print(*a[:x])
