import itertools
seed = []
with open("ImionaMęskie.txt", encoding="utf8") as file:
    #seed = file.readlines()
    for line in file:
        seed.append(line.rstrip())
    #    print(line)


max = len("adasdaddaddadadadsaadsasdasadfasdasfsasfasfaefasda")

wynik = itertools.product(seed, repeat=10)

for i in wynik:

    # print(i)
    print("".join(i))
    # print(seed)

# wynik.
