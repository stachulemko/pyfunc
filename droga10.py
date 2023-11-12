def droga(lista_polaczen):
    # Tworzenie grafu w postaci słownika, gdzie klucze to nazwy miejscowości, a wartości to zbiory miejscowości sąsiednich
    graf = {}
    for p in lista_polaczen:
        if p[0] not in graf:
            graf[p[0]] = set()
        graf[p[0]].add(p[1])
        if p[1] not in graf:
            graf[p[1]] = set()
        graf[p[1]].add(p[0])

    # Sprawdzenie, czy Ania i Zbyszek są w tym samym miejscu
    if 'A' == 'Z' or 'A' not in graf or 'Z' not in graf:
        return -1

    # Wyszukiwanie ścieżki między Anią i Zbyszkiem przy użyciu algorytmu BFS
    odleglosci = {'A': 0}
    kolejka = ['A']
    while kolejka:
        aktualne = kolejka.pop(0)
        for sasiad in graf[aktualne]:
            if sasiad not in odleglosci:
                odleglosci[sasiad] = odleglosci[aktualne] + 1
                kolejka.append(sasiad)
                if sasiad == 'Z':
                    return odleglosci[sasiad]

    # Nie udało się znaleźć ścieżki między Anią i Zbyszkiem
    return -1


print(droga([['D', 'E'], ['A', 'W'], ['G', 'Y'], ['X', 'Y'], ['W', 'X'], ['E', 'F'], ['F', 'G'], ['Z', 'B'], ['C', 'D'],
             ['B', 'C']])
      )
