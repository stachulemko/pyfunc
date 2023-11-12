def liczba_jasia(lista_liczb):
    # print(lista_liczb)
    # print(len(lista_liczb))
    piwot = len(lista_liczb)//2
    # print(piwot)
    if len(lista_liczb) == 0:
        return lista_liczb
    if len(lista_liczb) == 1:
        if lista_liczb[0] % 2 == 0:
            return lista_liczb
        else:
            return []
    if len(lista_liczb) == 2:
        if lista_liczb[0] % 2 == 0:
            return lista_liczb[:1]
        elif lista_liczb[1] % 2 == 0:
            return lista_liczb[1:]
        else:
            return []
    if lista_liczb[piwot] % 2 == 0:
        return liczba_jasia(lista_liczb[:piwot+1])
    else:
        return liczba_jasia(lista_liczb[piwot:])


assert liczba_jasia([5, 99, 3, 7, 111, 13, 4, 24, 4, 8]) == [4]
assert liczba_jasia([4]) == [4]
assert liczba_jasia([1, 3, 5, 4, 6, 8]) == [4]
assert liczba_jasia([4, 6, 8]) == [4]
assert liczba_jasia([1, 3, 5]) == []
assert liczba_jasia([]) == []
