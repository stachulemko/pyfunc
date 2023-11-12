def lamacz_plotkowego(szyfr):
    klucze_mozliwe = list(range(2, len(szyfr)))
    for i in klucze_mozliwe:
        # Generate a list of coordinates for the first key
        lista1 = list(range(1, i))
        # Generate a list of coordinates for the second key
        lista2 = list(range(1, len(szyfr) + 1))
        lista_wspolrzednych = []
        lista_wspolrzednych_kluczy_wszystkich = []
        licznik = 0
        licznik2 = 0
        for w in lista2:
            True
            for j in lista1:
                lista_wspolrzednych.append(j)
                lista_wspolrzednych.append(w)
                if i > 2:
                    licznik += 1
                else:
                    True
                if licznik == i:
                    lista1 = lista1[i:1]
                else:
                    True
                lista_wspolrzednych_kluczy_wszystkich.append(
                    lista_wspolrzednych)
        print(lista_wspolrzednych_kluczy_wszystkich)


lamacz_plotkowego("alamakota")
