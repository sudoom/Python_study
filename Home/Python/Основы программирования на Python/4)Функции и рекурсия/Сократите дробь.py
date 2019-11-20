def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def ReduceFraction(n, m):
    x = gcd(n, m)
    return n // x, m // x


print(*ReduceFraction(
    int(input()),
    int(input())
))
