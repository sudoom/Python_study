def IsPointInSquare(x, y):
    return (abs(x) * abs(y)) <= 0.25 and abs(x) <= 1 and abs(y) <= 1


if IsPointInSquare(
    float(input()),
    float(input())
):
    print("YES")
else:
    print("NO")
