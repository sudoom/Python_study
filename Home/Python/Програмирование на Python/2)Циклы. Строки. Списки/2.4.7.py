x = input()
i = 0
j = -len(x) + 1
k = 1
m = ""
while j < 0:
    if x[i] == x[j]:
        i += 1
        j += 1
        k += 1
    elif (x[i] != x[j]) or j == 0:
        m = m + str(x[i]) + str(k)
        k = 1
        i += 1
        j += 1
print(m)
