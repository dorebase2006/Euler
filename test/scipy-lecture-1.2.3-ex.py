wpi = 2
upper = 100000
for i in range(1, upper):
    wpi = wpi * (4 * (i ** 2)) / (4 * (i ** 2) - 1)
print(wpi)
