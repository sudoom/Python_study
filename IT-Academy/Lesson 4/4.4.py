start_dep = 1000
procent = float(input('Enter procent 0 to 25:'))
prpr = 1+procent/100
mon = 0
while start_dep < 1100:
    start_dep *= prpr
    mon += 1
print(mon, start_dep)
