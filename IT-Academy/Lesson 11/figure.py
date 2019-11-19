from math import pi


class FigureError(Exception):
    pass


def rect_perimetr(a, b):
    x = (a + b) * 2
    return x


def rect_area(a, b):
    x = a * b
    return x


def tri_perimetr(a, b, c):
    x = a + b + c
    if a < b+c and b < a+c and c < a+b:
        return x
    else:
        raise FigureError('Triangle undefined')


def tri_area(a, b, c):
    x = (((a+b+c)*(b+c-a)*(a+c-b)*(a+b-c))**(1/2))/4
    if a < b+c and b < a+c and c < a+b:
        return x
    else:
        raise FigureError('Triangle undefined')


def tra_perimetr(a, b, c, d):
    x = a + b + c + d
    if a < b+c+d and b < a+c+d and c < a+b+d and d < a+b+c:
        return x
    else:
        raise FigureError('Trapezoid undefined')


def tra_area(a, b, c, d):
    h = (c**2 - (((((c**2-d**2)/b-a)+b-a)**2)/4))**1/2
    x = ((a+b)/2)*h
    if a < b+c+d and b < a+c+d and c < a+b+d and d < a+b+c:
        return x
    else:
        raise FigureError('Trapezoid undefined')


def circle_perimetr(r):
    x = 2 * pi*r
    return x


def circle_area(r):
    x = pi*r**2
    return x


def square_area(a):
    x = a**2
    return x


def square_perimetr(a):
    x = 4*a
    return x
