n = int(input())
i = n
s = 0
if n <= 20:
    x = float(input())
    while 0 < i <= n:
        a = float(input())
        s += a * x**i
        i -= 1
    if i == 0:
        a = float(input())
        s += a
print(s)
