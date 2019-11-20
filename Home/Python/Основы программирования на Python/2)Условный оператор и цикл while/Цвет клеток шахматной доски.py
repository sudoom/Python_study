x1, y1 = int(input()), int(input())
x2, y2 = int(input()), int(input())
if (x1 + y1) % 2 == 0 and (x2 + y2) % 2 == 0:
    print("YES")
elif (x1 + y1) % 2 == 1 and (x2 + y2) % 2 == 1:
    print("YES")
else:
    print("NO")
