x = int(input())
i, k, m = 1, 1, 1
while i <= x:
    if i == x:
        print(k)
    i += 1
    m = i ** 2
    k += m
