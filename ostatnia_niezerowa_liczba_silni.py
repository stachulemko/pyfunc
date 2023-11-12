import sys


def obliczanie_silni(liczba):
    if liczba == 1:
        return 1
    else:
        return liczba * obliczanie_silni(liczba - 1)


def obliczanie_cyfry_z_liczby(*args):
    for y in args:
        wynik_silni = obliczanie_silni(y)
        while wynik_silni % 10 == 0:
            wynik_silni //= 10
        return wynik_silni % 10


def obliczanie_cyfry_z_liczby2(y):
    wynik_silni = obliczanie_silni(y)
    while wynik_silni % 10 == 0:
        wynik_silni //= 10
    return wynik_silni % 10
# obliczanie_cyfry_z_liczby(4, 1, 3, 5, 8)


# for y in (4, 1, 3, 5, 8):
    # print(obliczanie_cyfry_z_liczby2(y))
for line in sys.stdin:
    sys.stdout.write(str(obliczanie_cyfry_z_liczby2(int(line))))
