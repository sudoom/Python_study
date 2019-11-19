M = [[1, 2, 3, 4], [3, 4, 8, 6], [5, 4, 6, 9]]
p1 = int(input())
p2 = int(input())
counter = 0
for row in M:
    for numb in row:
        if numb >= p1 and numb <= p2:
            counter += 1
print(counter)
