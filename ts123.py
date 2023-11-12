def zad(x):
    while True:
        a = len(x)
        b = a // 2
        if b % 2 > 0:
            x = x[(x.index(b) + 1):]
        else:
            x = x[:(x.index(b) - 1)]
        if len(x) == 1:
            return x[0]


zad([5, 99, 3, 7, 111, 13, 4, 24, 4, 8])
