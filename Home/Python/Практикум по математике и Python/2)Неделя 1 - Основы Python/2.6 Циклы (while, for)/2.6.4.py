x = input()
x = x.split()
for i in x:
    if i[0] == "*":
        continue
    print(i)
