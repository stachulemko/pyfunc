file_path = 'plik.txt'
with open(file_path, 'r') as file:
    licznik=0
    for line in file:
        poz1 = line.find("#")
        print(line[:poz1])
        poz2 = line.find("'''")
        print(line[:poz2])
        

