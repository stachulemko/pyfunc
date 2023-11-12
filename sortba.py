s = [2, 1, 3, 1, 1]
z = len(s)
for i in s:
    e = s.index(i)
    if e < z-1:
        print(s[e+1])
        if i < s[e+1]:
            print("nie")
        else:
            s[e+1], s[e] = s[e], s[e+1]
            print("tak")
print(s)
