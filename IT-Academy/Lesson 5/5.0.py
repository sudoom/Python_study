def inputs():
    lists = []

    while True:
        i = input("Enter value: ")
        if i == "":
            break
        lists.append(i)
    return lists


def iter(k):
    dicts = {}

    for i in k:
        if i in dicts:
            dicts[i] += 1
        else:
            dicts[i] = 1
    return "most element: '{}' is repeated {} times".format(*max(dicts.items(), key=lambda x: x[1]))


print(iter(inputs()))
