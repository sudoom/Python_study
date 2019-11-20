def lagranj(n):
    t = list()
    for i in range(4):
        if n == 1:
            t.append(1)
            break
        s = int(n ** 0.5)
        n = n - s ** 2
        t.append(s)
    print(*t)


lagranj(int(input()))
