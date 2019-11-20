def power(a, n):
    if n == 0:
        return 1
    elif n < 0:
        return 1/(a**abs(n))
    else:
        return a ** n


print(power(
    float(input()),
    int(input())
))
