def C(n, k):
    if n == k or k == 0:
        return 1
    elif k == 1:
        return n
    return C(n - 1, k) + C(n - 1, k - 1)


print(C(
    int(input()),
    int(input())
))
