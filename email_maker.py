from itertools import combinations

# Wczytywanie elementów z plików
file_paths = ["E:\dev\no_name\pshishing\project_email_maker\names_and_surnames\ImionaMęskie.txt", "E:\dev\no_name\pshishing\project_email_maker\names_and_surnames\ImionaŻeńskie.txt", "E:\dev\no_name\pshishing\project_email_maker\names_and_surnames\NazwiskaMęskie.txt", "E:\dev\no_name\pshishing\project_email_maker\names_and_surnames\NazwiskaŻeńskie.txt", "E:\dev\no_name\pshishing\project_email_maker\słowa_polskie.txt", "E:\dev\no_name\pshishing\project_email_maker\znaki.txt"]
elements = []

for file_path in file_paths:
    with open(file_path, 'r') as file:
        file_elements = [line.strip() for line in file]
        elements.extend(file_elements)

# Wyświetlanie pojedynczych elementów
for element in elements:
    print(element)

# Wyświetlanie kombinacji dwuelementowych
combinations_2 = list(combinations(elements, 2))
for combination in combinations_2:
    print(list(combination))
    print(list(combination[::-1]))
