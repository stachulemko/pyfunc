
import itertools


def palindromy(x):
    l = []
    for i in range(1, x+1):
        if str(i) == str(i)[::-1]:
            l.append(i)
    combl3 = list(itertools.combinations(l, 3))
    for l3 in combl3:
        if sum(l3) == x:
            print(l3)
    """for i in l:
        for j in l:
            for k in l:
                if i != j and j != k and i != k:
                    if i+j+k == x:
                        print(i, j, k) """

    return l


print(palindromy(100))
