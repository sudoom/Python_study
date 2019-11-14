x = input()
if x == "int":
    i_1, i_2 = int(input()), int(input())
    if i_1 == i_2 == 0:
        print("Empty Ints")
    else:
        print(i_1 + i_2)
elif x == "str":
    s_1 = input()
    if s_1 == "":
        print("Empty String")
    else:
        print(s_1)
elif x == "list":
    l_1 = input().split()
    if len(l_1) == 0:
        print("Empty List")
    else:
        print(l_1[-1])
else:
    print("Unknown type")
