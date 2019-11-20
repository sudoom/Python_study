from math import atan


def f(x):
    return round(2 * atan(x), 3)


lim = f(99999999999999999999999)
print(lim)
