a = ['a', 'b', 'c']
b = [0 for i in range(5)]
b = [a[i] for i in b if a[i] else i]

print a
