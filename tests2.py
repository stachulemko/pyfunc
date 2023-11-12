

from os import remove


def p():
    imiona = ['kapus', 'papus', 'szistan', 'bella', 'vito']
    print(imiona)
    imiona.sort()
    print(imiona)
    try:
        imiona.remove("vito")
    except ValueError:
        print("brak imienia ")
    print(imiona)
    # imiona.remove("vito")
    imiona.reverse()
    print(imiona)


p()
