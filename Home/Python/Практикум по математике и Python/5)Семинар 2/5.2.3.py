from math import sin,cos,atan,exp


def derivative(f, x0=0):
    dx = 0.00001
    if f == sin:
        return round((sin(x0 + dx) - sin(x0)) / dx, 3)
    elif f == cos:
        return round((cos(x0 + dx) - cos(x0)) / dx, 3)
    elif f == atan:
        return round((atan(x0 + dx) - atan(x0)) / dx, 3)
    elif f == exp:
        return round((exp(x0 + dx) - exp(x0)) / dx, 3)


print(derivative(exp, 1))