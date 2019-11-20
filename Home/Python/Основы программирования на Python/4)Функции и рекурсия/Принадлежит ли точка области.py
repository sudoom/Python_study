def IsPointInArea(x, y):
    s = (x + 1) ** 2 + (y - 1) ** 2
    v = x + y
    t = y - 2 * x
    return (s <= 4 and v >= 0 and t >= 2) or (s >= 4 and v <= 0 and t <= 2)


if IsPointInArea(
        float(input()),
        float(input())
):
    print("YES")
else:
    print("NO")
