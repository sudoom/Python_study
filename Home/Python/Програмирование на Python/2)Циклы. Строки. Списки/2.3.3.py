a = int(input())
b = int(input())
c = int(input())
d = int(input())
for k in range(c, d + 1):
    print('\t', k, end='\t')
print()
for i in range(a, b + 1):
    print(i, end='')
    for j in range(c, d + 1):
        print('\t', i * j, end='\t')
    print()
