x = input()
if x.find("f") == -1:
    pass
elif x.find("f") == x.rfind("f"):
    print(x.find("f"))
else:
    print(x.find("f"), x.rfind("f"))
