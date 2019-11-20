def power(a, n):
    if n == 0:
        return 1
    elif n == 1:
        return a
    elif n % 2 == 0:
        return power(a ** 2, n // 2)
    elif n % 2 != 0:
        return a * power(a, n - 1)


print(power(
    float(input()),
    int(input())
))
