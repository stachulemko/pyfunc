def klocki(x):
    opa = 0
    wiersze = [[]]
    licznikgłowny = 0
    l = [[]]
    max = 1
    licznik = 0
    for i in x:
        # print(l)
        l[max-1].append(ord(i))
        licznik += 1
        if max == licznik:
            licznik = 0
            max = max+1
            if len(l) < max:
                p = []
                l.append(p)
    for o in l:
        for i in range(len(o)):
            #print(o, i, o[i], wiersze)
            if len(wiersze) < i+1:
                wiersze.append([])
                # print(wiersze)
            wiersze[i].append(o[i])
    for i in wiersze:
        for j in i:
            opa = opa+i
    if opa//len(j) == i[0]:
        licznikgłowny = licznikgłowny+1

    return licznikgłowny


print(klocki("ALAMAKRABY"))
