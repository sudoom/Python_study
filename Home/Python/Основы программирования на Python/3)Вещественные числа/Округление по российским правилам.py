from math import ceil, floor
x = float(input())
if 0 <= (x % 1) * 10 < 5:
    print(floor(x))
else:
    print(ceil(x))
