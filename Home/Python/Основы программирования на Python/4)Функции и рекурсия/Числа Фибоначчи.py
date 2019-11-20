def phib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return phib(n-2) + phib(n-1)


print(phib(int(input())))
