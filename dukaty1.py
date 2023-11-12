def dukaty(x):
    if x > 6:
        liczbaliczbpodzielnychprzez_6 = x//6
        sumadukatowpo_6 = (x//6)*8
        całasuma = (x-(x//6)*8)+(x//6)*8
        return całasuma


print(dukaty(20))
