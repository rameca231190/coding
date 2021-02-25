dollar = 900
percent = 0.15
total = 0
for i in range(0, 24):
    total = total + dollar
    k = total * percent
    total += k
print(total)