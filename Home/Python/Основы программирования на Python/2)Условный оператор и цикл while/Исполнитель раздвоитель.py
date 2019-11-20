x_1 = int(input())
x_2 = int(input())
while x_1 > x_2:
    if x_1 % 2 == 0 and x_1 // 2 >= x_2:
        x_1 //= 2
        print(":2")
    elif x_1 % 2 == 1 or x_1 > x_2:
        x_1 -= 1
        print("-1")
