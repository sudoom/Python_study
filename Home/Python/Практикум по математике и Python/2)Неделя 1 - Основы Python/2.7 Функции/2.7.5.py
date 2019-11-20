def dfactorial(n):
    if n % 2 == 0:
        if n == 0:
            return 1
        else:
            return n * dfactorial(n-2)
    elif n % 2 == 1:
        if n == 1:
            return 1
        else:
            return n * dfactorial(n-2)
