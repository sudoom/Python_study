def My_dec(f):
    def wapper():
        result = f()
        print(type(result))
        if type(result) in (list, dict, set, tuple):
            with open("1.json", "w") as rd:
                rd.write(str(result))
                return 1
        else:
            with open("2.txt", "w") as qt:
                qt.write(str(result))
                return 2
    return wapper


@ My_dec
def a():
    b = ('daf', 65)
    return b
a()
