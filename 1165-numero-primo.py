def nPrimo(num):
    cont = 0
    x = num
    y = num
    while y > 0:
        if x % y == 0:
            cont += 1
        y -= 1
    if cont == 2:
        return True
    else:
        return False

qnt = int(input())

for i in range(qnt):
    numero = int(input())
    if nPrimo(numero):
        print(numero, 'eh primo')
    else:
        print(numero, 'nao eh primo')