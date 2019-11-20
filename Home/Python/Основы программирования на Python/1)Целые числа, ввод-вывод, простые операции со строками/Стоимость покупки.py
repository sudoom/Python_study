rubles, coins, cakes = int(input()), int(input()), int(input())
sum_cakes = (rubles * 100 + coins) * cakes
print(sum_cakes // 100, sum_cakes % 100)
