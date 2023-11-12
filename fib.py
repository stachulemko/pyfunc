def main():
    lista = list(range(1, 10, 2))
    print(lista)
    print(len(lista))
    for element in lista:
        print(element)
    print(lista[4])
    print(lista[len(lista)-1])
    print(lista[-2])
    i = 0
    while i < len(lista):
        print(lista[i])
        i = i+1
   


main()
