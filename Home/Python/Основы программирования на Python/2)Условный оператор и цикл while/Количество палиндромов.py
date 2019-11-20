x = int(input())
y = 0
while x > 0:
    i = x
    k = 0
    while i > 0:
        k = k * 10 + i % 10
        i //= 10
    if x == k:
        y += 1
    x -= 1
print(y)
