import math
b = [i for i in range(20) if i > 5]
print(b)
c = [i**2 for i in range(20) if i % 2 == 1]
print(c)
d = [[i, j, c] for i in range(1, 10) for j in range(1, 10)
     for c in range(i, 15) if i**2+j**2 == c**2]
print(d)
print(math.sqrt(4))


e = [2 * i for i in range(1, 10) if i %
     3 != 0 and i % 2 != 0]
print(e)
#value_if_true if condition else value_if_false
f = []
for i in range(1, 10):
    if i % 3 != 0 and i % 2 != 0:
        f.append(i*2)
print(f)
