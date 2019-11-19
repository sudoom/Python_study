percent, rubble, coin = int(input()), int(input()), int(input())
coin += rubble * 100
count_coins = coin + coin * percent / 100 + 10 ** -9
print(int(count_coins//100), int(count_coins % 100))
