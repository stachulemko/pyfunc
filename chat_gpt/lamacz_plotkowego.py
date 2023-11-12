def generator_poz(dw, dk):
    poz = []
    flaga = True
    j = 0
    for i in range(dw):
        poz.append([j, i])
        if flaga:
            j += 1
        else:
            j -= 1

        if j == 0 or j == dk-1:
            flaga = not flaga
    poz.sort()
    return poz


def szyfruj(msg, poz):
    szyfr = ""
    for _, i in poz:
        szyfr += msg[i]
        # print(i)
        # print(szyfr)
    return szyfr


def deszyfruj(szyfr, poz):
    msg = ""
    lmsg = [None] * len(szyfr)
    j = 0
    for _, i in poz:
        lmsg[i] = szyfr[j]
        j += 1
    for ch in lmsg:
        msg += ch
    return msg


def genszyfr_szyfrowo(szyfr):
    szyfry = []
    dlugosc_szyfru = len(szyfr)
    for i in range(2, dlugosc_szyfru):
        szyfry.append(deszyfruj(szyfr, generator_poz(dlugosc_szyfru, i)))
    return szyfry


print(generator_poz(5, 2))
print(szyfruj("alamakota", generator_poz(9, 2)))
print(deszyfruj("aaalm", generator_poz(5, 2)))
print(genszyfr_szyfrowo("aaaoalmkt"))
