a, b, c = int(input()), int(input()), int(input())
maxX = max(a, b, c)
minN = min(a, b, c)
print(maxX, '\n', minN, '\n', (a + b + c)-maxX - minN, sep='')
