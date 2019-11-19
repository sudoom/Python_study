hours_1, minutes_1, seconds_1 = int(input()), int(input()), int(input())
hours_2, minutes_2, seconds_2 = int(input()), int(input()), int(input())
seconds_2_all = hours_2 * 3600 + minutes_2 * 60 + seconds_2
seconds_1_all = hours_1 * 3600 + minutes_1 * 60 + seconds_1
print(seconds_2_all - seconds_1_all)
