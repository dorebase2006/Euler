limit = 1000
sum = 0
for i in range(3, limit):
    if (i%3 == 0) or (i%5 == 0):
        sum = sum + i
print sum
