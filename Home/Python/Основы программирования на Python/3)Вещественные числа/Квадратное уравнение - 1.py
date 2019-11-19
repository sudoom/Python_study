a, b, c = float(input()), float(input()), float(input())
d = b ** 2 - 4 * a * c
x1, x2 = 0, 0
if d < 0:
    pass
elif d == 0:
    x1 = -b / (2 * a)
    print(x1)
elif d > 0:
    x1 = (-b-d**0.5)/(2*a)
    x2 = (-b+d**0.5)/(2*a)
    if a < 0:
        x1, x2 = x2, x1
    print(x1, x2)
