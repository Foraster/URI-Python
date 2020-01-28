op = input()
soma = 0
cont = 0

for i in range(12):
    for j in range(12):
        valor = float(input())
        if (j >= 7 and i < j and i + j >= 12):
            soma += valor
            cont += 1

if op == 'S':
    print("%.1f" % soma)
else:
    media = soma / cont
    print("%.1f" % media)