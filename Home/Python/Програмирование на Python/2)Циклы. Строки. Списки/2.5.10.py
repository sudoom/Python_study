x = input().split()
x = list(map(int, x))
y = list()
b = len(x)
for j in range(0, b):
    if b == 1:
        print(*x)
    elif j == 0:
        y.append(x[1] + x[-1])
    elif j == b-1:
        y.append(x[-2]+x[0])
    else:
        y.append(x[j-1]+x[j+1])
print(*y)
