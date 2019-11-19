n = int(input())
if 9 < n < 21 or n % 10 == 0 or n % 10 == 5 or n % 10 == 6 or n % 10 == 7 \
        or n % 10 == 8 or n % 10 == 9:
    print(n, "korov")
elif n % 10 == 1:
    print(n, "korova")
else:
    print(n, "korovy")
