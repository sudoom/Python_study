def numerics(n):
    return [int(i) for i in str(n)]


def kaprekar_step(L):
    x1 = sorted([str(i) for i in L])
    x2 = x1[::-1]
    x1 = "".join(x1)
    x2 = "".join(x2)
    return int(x2) - int(x1)


def kaprekar_loop(n):
    if len(set(numerics(n))) == 1:
        return n
#    while n <= 1000:
#        print("Ошибка! На вход подано число 1000")
#        return break
#    while str(n).count(str(n)[0]) == 4:
#        print("Ошибка! На вход подано число {} - все цифры одинаковые".format(n))
    print(n)
    if n == 6174:
        return n
    return kaprekar_loop(kaprekar_step(numerics(n)))


kaprekar_loop(
    int(input())
)