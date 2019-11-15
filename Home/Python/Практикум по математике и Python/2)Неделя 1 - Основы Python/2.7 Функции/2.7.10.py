def convert(L):
    return list(map(int, L))


def maxId(L):
    L = convert(L)
    b = max(L)
    return L.index(b)
