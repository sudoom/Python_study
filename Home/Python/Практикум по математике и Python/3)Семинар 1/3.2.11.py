n = int(input())


def donuts(n):
    text = "Всего пончиков: "
    if n <= 9:
        return text + str(n)
    return text + "много"


print(donuts(n))
