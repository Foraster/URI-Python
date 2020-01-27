valor = int(input())
print("N[0] =", valor)

for i in range(1, 10):
    valor *= 2
    print("N[{}] = {}".format(i, valor))
