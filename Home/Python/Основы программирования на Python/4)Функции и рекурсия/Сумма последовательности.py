def summa(x):
    y = x
    if x != 0:
        x = int(input())
        y += summa(x)
    return y


print(summa(
    int(input())
))
