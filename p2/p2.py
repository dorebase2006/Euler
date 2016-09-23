lim = 4000000
fib1 = 1
fib2 = 2
fibcur = fib1 + fib2
sum = 2
while fibcur < lim:
    if fibcur % 2 == 0:
        sum += fibcur
    fib1, fib2 = fib2, fibcur
    fibcur = fib1 + fib2
print(sum)