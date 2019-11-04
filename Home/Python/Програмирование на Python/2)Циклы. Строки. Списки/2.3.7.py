a, b = int(input()), int(input())
s = 0
x = 0
for i in range(a, b + 1):
    if i % 3 == 0:
        s += i
        x += 1
print(s/x)
