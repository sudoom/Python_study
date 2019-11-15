x = input().split()
x = list(map(int, x))
b = len(x)
t = list()
for i in range(0, len(x)):
    y = x.count(x[i])
    if y > 1:
        t.append(x[i])
print(*set(t))
