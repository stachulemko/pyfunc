from audioop import avg
import random


def main():
    l = []
    for i in range(10):
        l.append(random.randint(1, 100))
    print(l)
    print(max(l))
    print(min(l))
    print(sum(l))
    l1 = list(range(2, 99, 3))
    print(l1)
    avg = sum(l1)/len(l1)
    print(avg)


main()
