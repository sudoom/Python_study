x = input()
print(x[:x.rfind("h")] + x[x.find("h")+1:])
