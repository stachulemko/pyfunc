def kupa(x):
    w = max(x)
    lista = [0] * (w + 2)
    for i in x:
        lista[i] += 1
    # print(lista)
    lista.remove(0)  # Usunięcie zera z listy
    # Poprawka: Używamy range(len(lista) - 1) aby nie wyjść poza zakres
    for k in range(len(lista) - 1):
        elk = lista[k + 1]
        elk += lista[k]
        lista[k + 1] = elk  # Aktualizacja wartości w liście
    lista.insert(0, 0)
    # print(lista)
    nowalista = [0]*(len(x)+1)
    for j in x:
        print(j)
        nowalista[lista[j]] += j
        lista[j] -= 1
    print(nowalista)


kupa([1, 4, 1, 2, 7, 5, 2])
#done !!!