x = input()
if x == 'треугольник':
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a+b+c)/2
    s = (p*(p-a)*(p-b)*(p-c))**0.5
    print(s)
elif x == 'прямоугольник':
    a = int(input())
    b = int(input())
    s = a*b
    print(s)
elif x == 'круг':
    r = int(input())
    s = 3.14 * r**2
    print(s)
