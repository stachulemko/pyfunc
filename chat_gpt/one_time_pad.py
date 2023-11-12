def liczby_pierwsze(liczby):
    for i in liczby:
        if i % 2 == int(i) or i % 3 == int(i) or i == 3 or i == 2:
            print("TAK")
        else:
            print("NIE")


liczby_pierwsze([3, 11, 1, 4])
