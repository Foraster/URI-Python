op = input()
soma = 0

for i in range(12):
    for j in range(12):
        valor = float(input())
        if (i + j) <= 10:
            soma += valor

if op == 'S':
    print("%.1f" % soma)
else:
    media = soma / 66.0
    print("%.1f" % media)