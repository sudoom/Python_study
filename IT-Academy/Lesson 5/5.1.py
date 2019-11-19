a = [[1, 2, 3], [7, 8, 9]]
summ = 0
cou = 0
for i in a:
    cou += len(i)
for row in a:
    for elem in row:
        summ += elem
print('Среднее арифметическое равно:', summ/cou)
