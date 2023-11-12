def szyfr(x):
    liczba = 0
    lliczba = 0
    listakoncowa = ""
    liczby = []
    l = []
    while x > 0:
        r = x % 100
        x = x//100
        l.append(r)
    for i in l[::-1]:
        print(i)
        if i < 41:
            while liczba+20 != i:
                liczba = liczba+1
            listakoncowa += chr(96+liczba)
            liczba = 0
        else:
            while lliczba+40 != i:
                lliczba = lliczba+1
            listakoncowa += chr(109+lliczba)
            lliczba = 0
    return listakoncowa


print(szyfr(2328214731212221225230212729))
