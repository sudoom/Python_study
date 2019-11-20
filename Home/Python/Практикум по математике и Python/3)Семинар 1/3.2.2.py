from math import exp


def f(x):
    return exp(x)


def def_e(x):
    dx = 0.00001
    return round((f(x + dx) - f(x)) / dx, 3)

