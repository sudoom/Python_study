a1, b1, c1 = int(input()), int(input()), int(input())
a2, b2, c2 = int(input()), int(input()), int(input())
if a1 > b1:
    (a1, b1) = (b1, a1)
if b1 > c1:
    (b1, c1) = (c1, b1)
if a1 > b1:
    (a1, b1) = (b1, a1)
if a2 > b2:
    (a2, b2) = (b2, a2)
if b2 > c2:
    (b2, c2) = (c2, b2)
if a2 > b2:
    (a2, b2) = (b2, a2)
x1 = a1 // a2
x2 = b1 // b2
x3 = c1 // c2
print(x1*x2*x3)
