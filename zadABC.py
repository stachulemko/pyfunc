def abc(nasz):
    licznik = 0
    nasz1 = []
    for x in nasz:
        nasz1.append(x)
    for i in range(len(nasz)-1):
        l = nasz[i]
        if l == 'c' or l == 'z':
            b = nasz[i+1]
            if b == 'n':
                # nasz1.remove(i+1)
                licznik = licznik + 1
            else:
                True

    return licznik


print(abc('zzzznnnnz'))
