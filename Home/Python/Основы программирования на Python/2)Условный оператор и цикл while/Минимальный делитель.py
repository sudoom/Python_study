n = int(input())
i = 1
k = 2
while i < k:
    if n % k == 0:
        print(k)
        break
    else:
        i = i + 1
        k = k + 1
