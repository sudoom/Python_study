def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def sf(n):
    if factorial(n) == 1:
        return 1
    else:
        return factorial(n) * sf(n - 1)
