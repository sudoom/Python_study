x = int(input())
y = x
t = [y]
while y != 0:
    x = int(input())
    t.append(x)
    y += x
t = [i**2 for i in t]
print(sum(t))
