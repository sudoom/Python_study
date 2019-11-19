x_1 = x_2 = 1
n = int(input()) - 2
while n > 0:
    x_1, x_2 = x_2, x_1 + x_2
    n -= 1
print(x_2)
