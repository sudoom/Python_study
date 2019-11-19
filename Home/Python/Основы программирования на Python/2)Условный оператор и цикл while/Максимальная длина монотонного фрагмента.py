x = int(input())
i = k = m = 0
while x != 0:
    y = x
    x = int(input())
    if x > y:
        i += 1
    elif x < y:
        m += 1
    elif x == y:
        i += 0
        m += 0
    elif i > m:
        k = i
        i = 0
    elif m > i:
        k = m
        m = 0
    else:
        i = 0
        m = 0
    print("i=", i, "m=", m, "k=", k)
print(k)
