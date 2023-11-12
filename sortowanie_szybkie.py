import random


def sortowanie_szybkie(lista_do_posortowania):
    if len(lista_do_posortowania) <= 1:
        return None
    else:

        print("max", max)
        piwot = random.randint(0, max)
        lista_do_posortowania[piwot], lista_do_posortowania[-1] = lista_do_posortowania[-1], lista_do_posortowania[piwot]
        b = 0
        a = 0
        for i in lista_do_posortowania:
            print(a, b)
            if lista_do_posortowania[a] > lista_do_posortowania[-1]:
                a = a+1
            else:
                lista_do_posortowania[b], lista_do_posortowania[a] = lista_do_posortowania[a], lista_do_posortowania[b]
                a = a+1
                b = b+1

        sortowanie_szybkie(lista_do_posortowania[0: piwot])
        if piwot < max:
            sortowanie_szybkie(lista_do_posortowania[piwot+1: max])
        return lista_do_posortowania


print(sortowanie_szybkie([6, 1, 8, 4, 5, 2, 7, 3, 9]))
