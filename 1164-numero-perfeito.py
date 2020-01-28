def nPerfeito(num):
    vet = []
    x = num
    y = num-1
    while y > 0:
        if x % y == 0:
            vet.append(y)
        y -= 1
    if sum(vet) == num:
        return True
    else:
        return False

qnt = int(input())

for i in range(qnt):
    numero = int(input())
    if numero == nPerfeito(numero):
        print(numero, 'eh perfeito')
    else:
        print(numero, 'nao eh perfeito')