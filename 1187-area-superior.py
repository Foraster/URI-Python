op = input()
soma = 0
cont = 0

for i in range(12):
    if i == 5:
        break
    for j in range(12):
        valor = float(input())
        if (j - i >= 1 and j + i <= 10):
            soma += valor
            cont += 1

if op == 'S':
    print("%.1f" % soma)
else:
    media = soma / cont
    print("%.1f" % media)