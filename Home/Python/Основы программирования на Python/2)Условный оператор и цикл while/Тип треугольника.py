a, b, c = int(input()), int(input()), int(input())
if a + b <= c or\
        a + c <= b \
        or b + c <= a:
    print("impossible")
elif c ** 2 == a ** 2 + b ** 2 or\
        a ** 2 == c ** 2 + b ** 2 or\
        b ** 2 == c ** 2 + a ** 2:
    print("rectangular")
elif c ** 2 > a ** 2 + b ** 2 or\
        a ** 2 > c ** 2 + b ** 2 or\
        b ** 2 > c ** 2 + a ** 2:
    print("obtuse")
elif c ** 2 < a ** 2 + b ** 2 or\
        a ** 2 < c ** 2 + b ** 2 or\
        b ** 2 < c ** 2 + a ** 2:
    print("acute")
