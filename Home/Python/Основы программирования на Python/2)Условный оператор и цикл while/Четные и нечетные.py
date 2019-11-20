a, b, c = int(input()), int(input()), int(input())
if a % 2 == 0 and (b % 2 == 1 or c % 2 == 1) or \
        b % 2 == 0 and (a % 2 == 1 or c % 2 == 1) or \
        c % 2 == 0 and (a % 2 == 1 or b % 2 == 1):
    print("YES")
else:
    print("NO")
