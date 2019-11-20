n = int(input())
k = 1
i = 0
while k <= n:
    if n == 1:
        print(0)
        break
    k = 2 * k
    i = i + 1
    if k == n:
        print(i)
        break
if k > n:
    print(i)
