n, m = int(input()), int(input())
k = int(input())
if (k % n == 0 or k % m == 0) and k <= m * n:
    print("YES")
else:
    print("NO")
