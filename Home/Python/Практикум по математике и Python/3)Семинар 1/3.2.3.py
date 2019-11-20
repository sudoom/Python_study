def even_indeces(l):
    t = list()
    for i in range(len(l)):
        if i % 2 == 0:
            t.append(l[i])
    return t
