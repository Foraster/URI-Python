qnt = int(input())
soma = 0

for i in range(qnt):
    cod, q = map(int, input().split())
    if cod == 1001:
        soma += 1.50 * q
    elif cod == 1002:
        soma += 2.50 * q
    elif cod == 1003:
        soma += 3.50 * q
    elif cod == 1004:
        soma += 4.50 * q
    elif cod == 1005:
        soma += 5.50 * q

print('%.2f' % soma)