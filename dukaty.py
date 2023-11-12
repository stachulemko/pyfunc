def dukaty(x):
    if x >= 5:
        a = x//5
        c = a*7
        b = x-a*5
        g = c+b
        # print(g)
        if g >= 50:
            h = 3*g//4
            print(g-h)
#             licznik_50 = g//50
#             liczba_dni_50 = 38
#             suma_wszystkigo = g-g*liczba_dni_50
#             if suma_wszystkigo >= 5:
#                 h = suma_wszystkigo//5
#                 j = h*7
#                 k = suma_wszystkigo-a*5
#                 l = j+k
#                 return l
#             else:
#                 return suma_wszystkigo
#         else:
#             return g
#     else:
#         return x


# # print(g)
# print(dukaty(36))


def dukaty2(x):
    skarbonka = 0
    for i in range(1, x+1):
        skarbonka = skarbonka+1
        if i % 5 == 0:
            skarbonka = skarbonka+2
        if skarbonka >= 50:
            skarbonka = skarbonka-((skarbonka*3)//4)
        print(i, skarbonka)
    return skarbonka


print(dukaty2(1234))
