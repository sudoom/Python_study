def IsPointInSquare(x, y):
    return abs(x) <= 1 and abs(y) <= 1


if IsPointInSquare(
    float(input()),
    float(input())
):
    print("YES")
else:
    print("NO")
