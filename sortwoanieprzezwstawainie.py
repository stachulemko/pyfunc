from re import A


tab = [8, 2, 1, 9, 5]
for i in range(1, len(tab)):
    j = i
    while j > 0 and tab[j-1] > tab[j]:
        tab[j-1], tab[j] = tab[j], tab[j-1]
        j = j-1
print(tabs)
