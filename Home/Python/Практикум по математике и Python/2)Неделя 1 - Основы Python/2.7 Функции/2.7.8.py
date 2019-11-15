def translate(x, n=2):
    if x == 0:
        return str(x % n)
    else:
        return str(translate(x // n, n)) + str(x % n)
