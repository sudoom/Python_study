x = int(input())
m = x
v = 1
while x != 0:
    x = int(input())
    if x == 0:
        break
    if x == m:
        v += 1
    if x > m:
        v = 1
        m = x
print(v)
