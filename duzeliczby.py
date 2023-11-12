def duzeliczby(x, y):
    for i in range(1, 1000):
        if i**y > x:
            print((i-1)**y)


print(duzeliczby(90972061672647417382949994702882855264900000, 2))
