def litera(x):
    l = []   # lista nie poi
    k = []

    z = []

    for i in x:
        if i not in l:
            l.append(i)
    # print(l)

    for i in l:
        k.append(x.count(i))

    # print(k)
    u = max(k)
    # print(u)

    for i in range(len(k)):
        if k[i] == u:
            z.append(i)
    g = []
    for i in z:
        g.append(l[i])
    # print(g)
    return g

    # print(m)


print(litera("bacdefghijklmnopqrstuvwxyzaasdafnbbbbnbssjshjgsehfawhaaafheufeueeefefasdafafafadfafafa"))
