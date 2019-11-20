x = int(input())
y = x
while True:
    x = input()
    if x == "The End":
        break
    x = int(x)
    y += x
print(y)
