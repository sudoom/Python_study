x = int(input())
b = [x]
s, y = 0, 0
while x != 0:
    x = int(input())
    if x == 0:
        break
    b.append(x)
for i in b:
    s += i
s = s / len(b)
for i in b:
    y += (i-s)**2
sigma = (y/(len(b)-1))**0.5
print(sigma)
