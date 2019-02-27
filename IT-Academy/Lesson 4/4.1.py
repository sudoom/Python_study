def check_1():
    x = []
    for i in range(65, 91):
        x.append(chr(i))
    for j in range(97, 123):
        x.append(chr(j))
    x.append(chr(95))
    b = tuple(x)
    return b


def check_2():
    x = []
    for i in range(65, 91):
        x.append(chr(i))
    for j in range(97, 123):
        x.append(chr(j))
    for k in range(48, 58):
        x.append(chr(k))
    x.append(chr(95))
    b = set(x)
    return b


first_str = input("Enter your word please:")
new_str = first_str[1:]
new_str = set(new_str)
if first_str.startswith(check_1()) and new_str.difference(check_2()) == set():
    print("Okay, your word is identificator")
else:
    print("Check your word please")
