def wyszukiwanie_binarne(l, n):
    piwot = len(l)//2
    if piwot > n:
        j = l[::piwot]
        for i in j:
            if i == n:
                print(l.index(i))
    else:
        j = l[piwot::]
        for i in j:
            if i == n:
                print(l.index(i))


wyszukiwanie_binarne([1, 2, 3, 4, 5], 5)
