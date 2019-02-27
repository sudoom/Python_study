take_string = input()
string_to_list = take_string.split()
max_len = max(string_to_list, key=len)
take_len = len(max_len)
for i, e in enumerate(string_to_list):
    if len(e) == take_len:
        print(i)
