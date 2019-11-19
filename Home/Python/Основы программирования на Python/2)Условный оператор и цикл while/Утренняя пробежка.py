x, y = int(input()), int(input())
i = 1
while x <= y:
    if x == y:
        print(i)
        break
    x = x * 1.1
    i = i + 1
if x > y:
    print(i)
