n = int(input())
hours = n // 3600
minutes = n - hours * 3600
minutes_w = str(minutes // 60 // 10) + str(minutes // 60 % 10)
seconds = minutes % 60
seconds_w = str(seconds // 10) + str(seconds % 10)
print(hours % 24, minutes_w, seconds_w, sep=":")
