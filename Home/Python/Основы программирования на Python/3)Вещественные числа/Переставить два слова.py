x = input()
y = x.find(" ")
print(x[y+1:] + " " + x[:y])
