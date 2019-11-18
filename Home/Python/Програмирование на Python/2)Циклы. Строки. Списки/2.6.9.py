lst = input().split()
lst = list(map(int, lst))
x = int(input())
d = list()
for i in range(len(lst)):
    if lst[i] == x:
        d.append(i)
if len(d) == 0:
    print("Отсутствует")
else:
    print(*d)
