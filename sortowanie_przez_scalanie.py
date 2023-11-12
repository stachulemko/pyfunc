def listy_poz(poz,list):
    



def scalanie(x, y):
    l = []
    pozx_max = len(x) - 1
    pozy_max = len(y) - 1
    pozx = 0
    pozy = 0
    while not (
        pozx > pozx_max and pozy > pozy_max
    ):  # kresc sie dopoki obie nie sa puste
        if pozy > pozy_max:  # lista y jest pusta a lista x nie
            l.append(x[pozx])
            pozx += 1
        elif pozx > pozx_max:  # lista x jest pusta a lista y nie
            l.append(y[pozy])
            pozy += 1
        elif x[pozx] < y[pozy]:  # obie nie sa puste i mniejszy jest element z x
            l.append(x[pozx])
            pozx += 1
        else:
            l.append(y[pozy])  # obie nie sa puste i mniejszy jest element z y
            pozy += 1
    return l


print(scalanie([1, 2], [3, 4]))