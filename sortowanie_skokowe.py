def sortowanie_skokowe(l, e):
    n = 0
    w = 3
    liczba_krokow = 0
    while not w >= e:
        n = n+3
        w = w+3
        liczba_krokow += 1

    l = l[n:w]
    for i in l:
        if i == e:
            print("jest")


print(sortowanie_skokowe([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], 12))
