def pap():
    z = 1
    lista = []
    for i in range(10):
        col = []
        for j in range(10):
            # col.append(0)
            if (i == j):
                col.append(z)
                z = z+1
            else:
                col.append(0)
        lista.append(col)

    print(*lista, sep="\n")


# pap()


# def pap1():
#    lista = []
#    for i in range(0, 9):
#        col = [1, 2, 3, 4]
#        print(len(col))
#        for j in range(0, 9):
#            if (i == j):
#                col[j] = 1
#            else:
#               col[j] = 0
#            lista.append(col)
#    print(lista)


# pap1()

N = 10
#t = [[0 for i in range(N)] for j in range(N)]
t1 = [[1 for i in range(N)] for j in range(N)]
t2 = [[5 for i in range(N)] for j in range(N)]
suma = [[0 for i in range(N)] for j in range(N)]
print(*t1, sep="\n")
print(*t2, sep="\n")
for i in range(N):
    for j in range(N):
        suma[i][j] = t2[i][j]*t1[i][j]
print(*suma, sep="\n")
#t[6][1] = 6
# for c in range(N):
#    t[c][N-c-1] = 1
#print(*t, sep="\n")
