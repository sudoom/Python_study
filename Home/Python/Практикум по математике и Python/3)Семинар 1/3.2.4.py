def even_elements(l):
    t = list()
    for i in range(len(l)):
        if l[i] % 2 == 0:
            t.append(l[i])
    return t
