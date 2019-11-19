x = int(input())
k = 0
m = x
while x != 0:
    x = int(input())
    if x > m:
        k += 1
    m = x
print(k)
