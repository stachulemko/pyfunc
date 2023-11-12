file_path = 'plik.txt'
with open(file_path, 'r') as file:
    for line in file:
        poz1 = line.find("#")
        print(line[:poz1])

