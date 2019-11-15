a, b, c = int(input()), int(input()), int(input())
p = a + b + c
p_half = p / 2
s = (p_half*(p_half-a)*(p_half-b)*(p_half-c))**0.5
print(p)
print(s)
