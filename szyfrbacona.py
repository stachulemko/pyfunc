from turtle import *
alfabet = ["aaaaa", "aaaab", "aaaba", "aaabb", "aabaa", "aabab", "aabba",
           "aabbb", "abaaa", "abaaa", "abaab", "ababa", "ababb", "abbaa", "abbab", "abbba",
           "abbbb", "baaaa", "baaab", "baaba", "baabb", "baabb", "babaa", "babab", "babba",
           "babbb"]


def kw(size):
    for i in range(4):
        fd(size)
        rt(90)


def kol(size, schemat):
    for j in schemat:
        if j == 'a':
            fillcolor("yellow")
        elif j == "b":
            fillcolor("red")
        kw(size)
        fd(size)
        end_fill()


def szyfrbacona(szyfrogram):
    s = 700/len(szyfrogram)
    if s > 80:
        s = 80

    up()
    goto(-350, -200)
    down()

    for i in szyfrogram:
        print(i)
        x = ord(i)-65
        print(x)
        y = alfabet[x]
        lt(90)
        fd(s)
        kol(s, y)
        bk(6*s)
        rt(90)
        fd(s)
        lt(90)
        fd(s)


# print(szyfrbacona('GODZINAKODOWANIA'))
    for i in range(700/s):
        lt(90)
        up()
        fd(20)
        down()
        kol(20, "aaaaa")
        bk(5*20)
        rt(90)
        fd(20)
        lt(90)
        kol(20, "aaaaa")
# kw(20)


exitonclick()
