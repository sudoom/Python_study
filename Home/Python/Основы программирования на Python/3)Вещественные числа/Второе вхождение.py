x = input()
y = x.find("f")
if y == -1:
    print("-2")
elif y == x.rfind("f"):
    print("-1")
else:
    print(x.find("f", y+1))
