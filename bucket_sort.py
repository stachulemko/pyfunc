def buket_sort(s):
    w = []
    l = []
    for i in range(1, len(s)):
        w.append([i])

    for j in s:
        numer_liczby = j*10//1
        w[numer_liczby].append(j)
    for k in w:
        k.sort()
        l.append(k)
    return w


print(buket_sort([0.897, 0.552]))
