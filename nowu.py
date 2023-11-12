def main():
    imiona = ["ela", "ala", "maja", "jon"]
    imie = input("podaj imie:")
    poz = int(input("podaj miejce połozenia:"))
    # imiona.append(imie)
    imiona.insert(poz, imie)
    print(imiona, "nowa lista ")
    


main()
