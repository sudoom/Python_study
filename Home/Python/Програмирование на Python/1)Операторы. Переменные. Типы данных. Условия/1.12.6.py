x = int(input())
if 5 <= x % 10 <= 10 or x % 10 == 0 or 11 <= x % 100 <= 14:
    print(x, 'программистов')
elif 2 <= x % 10 <= 4:
    print(x, 'программиста')
else:
    print(x, 'программист')
