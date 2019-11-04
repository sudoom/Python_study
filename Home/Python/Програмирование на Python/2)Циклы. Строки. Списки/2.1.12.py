a = int(input())
b = int(input())
c = 1
while c != 0:
    if c % a == 0 and c % b == 0:
        print(c)
        break
    else:
        c += 1
