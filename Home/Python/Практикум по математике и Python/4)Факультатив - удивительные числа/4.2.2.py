def kaprekar_step(L):
    x1 = sorted([str(i) for i in L])
    x2 = x1[::-1]
    x1 = "".join(x1)
    x2 = "".join(x2)
    return int(x2)-int(x1)
