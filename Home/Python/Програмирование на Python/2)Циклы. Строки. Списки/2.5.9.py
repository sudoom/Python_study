x = input().split()
x = list(map(int, x))
k = 0
for i in x:
    k = i + k
print(k)
