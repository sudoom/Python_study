def IsPointInCircle(x, y, xc, yc, r):
    v = ((xc-x)**2+(yc-y)**2)**0.5
    return v <= r


if IsPointInCircle(
    float(input()),
    float(input()),
    float(input()),
    float(input()),
    float(input())
):
    print("YES")
else:
    print("NO")
