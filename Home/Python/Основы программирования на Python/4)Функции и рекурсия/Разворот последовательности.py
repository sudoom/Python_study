def rev():
    x = int(input())
    if x != 0:
        rev()
        print(x)
    elif x == 0:
        print(0)


rev()
