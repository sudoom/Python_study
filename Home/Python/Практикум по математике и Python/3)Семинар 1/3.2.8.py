def front_x(words):
    x_first = list()
    x_last = list()
    for i in words:
        if i == "":
            x_last.append(i)
        elif i[0] == "x":
            x_first.append(i)
        else:
            x_last.append(i)
    return sorted(x_first) + sorted(x_last)
