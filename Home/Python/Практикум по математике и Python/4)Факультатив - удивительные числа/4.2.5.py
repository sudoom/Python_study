def numerics(n):
    return [int(i) for i in str(n)]


n = 2222
if len(set(numerics(n))) == 1:
    print(5)

