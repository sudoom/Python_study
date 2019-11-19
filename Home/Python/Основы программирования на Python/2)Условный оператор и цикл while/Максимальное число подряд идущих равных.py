x = int(input())
i = k = 1
while x != 0:
    y = x
    x = int(input())
    if x == y:
        i += 1
    elif i > k:
        k = i
        i = 1
    else:
        i = 1
print(k)
