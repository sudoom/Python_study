x = int(input())
m = x
v = 0
while x != 0:
    x = int(input())
    if x == 0:
        break
    if x >= m:
        v = m
        m = x
    elif m >= x >= v:
        v = x
print(v)
