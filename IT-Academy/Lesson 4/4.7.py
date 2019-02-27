enter_str = input("Введите строку:")
enter_chr = input("Введите символ:")
str_to_list = list(enter_str)
check_list = []
for i, j in enumerate(str_to_list):
    if j == enter_chr:
        str_to_list[i] = enter_chr.upper()
        for k in [i]:
            check_list.append(k)
print(str_to_list[:int((max(check_list)))])
