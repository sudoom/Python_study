percent, rubble = int(input()), int(input())
coin, year = int(input()), int(input())
i = 1
while i <= year:
    coin += rubble * 100
    count_coins = coin + coin * percent / 100
    i += 1
    rubble = int(count_coins//100)
    coin = int(count_coins % 100)
print(rubble, coin)
