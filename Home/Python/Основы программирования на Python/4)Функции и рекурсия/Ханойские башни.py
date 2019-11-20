def hanoi(n, x=1, y=3, b=2):
    if n != 0:
        hanoi(n - 1, x, b, y)
        print(n, x, y)
        hanoi(n - 1, b, y, x)


hanoi(int(input()))
