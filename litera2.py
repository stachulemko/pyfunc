def litera(txt):
    g = {}
    for l in txt:
        if l in g:
            g[l] += 1
        else:
            g[l] = 1
    a = max(g.values())
    wynik = []
    for key, val in g.items():
        if val == a:
            wynik.append(key)
    return wynik


print(litera("julkalubipsy"))
