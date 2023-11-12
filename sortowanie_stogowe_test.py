def heap_sort(l):
    # Odwrócenie listy
    l = l[::-1]
    
    # Przejście po wszystkich elementach, oprócz ostatniego
    for i in range(len(l) - 1):
        # Przejście po każdym elemencie w i-tej liście
        for j in range(len(l[i])):
            # Sprawdzenie, czy j jest nieparzyste i czy wartość na pozycji j w i-tej liście jest większa niż w (i+1)-tej liście
            if j % 2 > 0 and l[i][j] > l[i+1][j]:
                # Zamiana wartości
                l[i][j], l[i+1][j] = l[i+1][j], l[i][j]
                
                # Sortowanie bąbelkowe w i-tej liście
                for k in range(len(l[i]) - 1):
                    if l[i][k] > l[i][k+1]:
                        l[i][k], l[i][k+1] = l[i][k+1], l[i][k]
            # Jeśli j jest parzyste
            elif j % 2 == 0:
                # Sortowanie bąbelkowe w i-tej liście
                for w in range(len(l[i]) - 1):
                    if l[i][w] > l[i][w+1]:
                        l[i][w], l[i][w+1] = l[i][w+1], l[i][w]
    
    # Odwrócenie listy z powrotem i zwrócenie wyniku
    return l[::-1]


# Przykład użycia
print(heap_sort([[1], [2, 3], [4, 5, 6, 7], [8, 9, 10]]))
