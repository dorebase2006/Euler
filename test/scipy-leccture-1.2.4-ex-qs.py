def quicksort(x):
    if len(x) < 2:
        return x
    else:
        less = []
        more = []
        for i in x[1:len(x)]:
            if i <= x[0]:
                less.append(i)
            else:
                more.append(i)

        return quicksort(less) + [x[0]] + quicksort(more)

l = [1, 2, 3, 4, 5, 6, 7]
print(quicksort(l))
