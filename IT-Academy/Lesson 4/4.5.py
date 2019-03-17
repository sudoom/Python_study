x = list(input())
for i, j in enumerate(x):
    if j == '0':
        x.pop(i)
        x.append('-1')
print(x)
