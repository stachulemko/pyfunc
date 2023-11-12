def cezar(teskt, przesuniecie):
    szyfr = ""
    ofset = 97
    for znak in teskt:
        kod = (ord(znak)+przesuniecie) % 255
        szyfr += (chr(kod))
    return szyfr


s = cezar("Ala ma Kota.", 2)
print(s)
t = cezar(s, -2)
print(t)
