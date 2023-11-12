def zad(x):
    while len(x) > 1:
        a = len(x)-1
        b = a//2
        print(b)
        if x[b] % 2 > 0:
            x = x[(b+1):]
        else:
            x = x[:(b-1)]

        print(x)


zad([1, 2])
