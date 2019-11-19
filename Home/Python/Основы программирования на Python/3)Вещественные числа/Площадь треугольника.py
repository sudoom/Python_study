x, y, z = float(input()), float(input()), float(input())
p = (x + y + z) / 2
s = (p*(p-x)*(p-y)*(p-z))**0.5
print(s)
