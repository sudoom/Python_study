def perimetr(x1, y1, x2, y2, x3, y3):
    ab = ((x2-x1)**2+(y2-y1)**2)**0.5
    bc = ((x3-x2)**2+(y3-y2)**2)**0.5
    ac = ((x3-x1)**2+(y3-y1)**2)**0.5
    return ab + bc + ac


print(perimetr(float(input()),
               float(input()),
               float(input()),
               float(input()),
               float(input()),
               float(input())
               ))
