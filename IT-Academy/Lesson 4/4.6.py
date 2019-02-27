x_str = "-1 0 15 65 78 -55"
x_list = x_str.split()
x_intlist = list(map(int, x_list))
print(sorted(x_intlist))
