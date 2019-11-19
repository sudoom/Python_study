y = int(input())
if y == 0:
    print(0)
else:
    x_1, x_2 = 0, 1
    n = 1
    while x_2 <= y:
        if x_2 == y:
            print(n)
            break
        x_1, x_2 = x_2, x_1 + x_2
        n += 1
    else:
        print(-1)
