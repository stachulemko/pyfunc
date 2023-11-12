import random
n = 100
suma = 0
min = 101
max = -1
for _ in range(n):
    x = random.randint(0, 100)
    print(x)
    if x < min:
        min = x
    if x > max:
        max = x
    suma = suma+x
print(min, max)
avg = suma/n
print(avg)
