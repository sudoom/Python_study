x = input()
y = x[x.find("h", x.find("h")+1):x.rfind("h")]
y = y.replace("h", "H")
print(x[:x.find("h", x.find("h")+1)] + y + x[x.rfind("h"):])
