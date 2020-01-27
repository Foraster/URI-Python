# Uri 1248, Escrito por: Alex Lares

qnt = int(input())
i = 0

while i < qnt:

    dieta = input()
    cafe = input()
    almoco = input()
    janta = cafe + almoco

    # Verifica se existe letra a mais:
    for letra in range(len(janta)):
        if janta[letra] not in dieta:
            dieta = 'CHEATER'
            break
        else:
            dieta = dieta.replace(janta[letra], '')

    # Se nao existir, arruma em ordem alfabetica:
    if dieta != 'CHEATER':
        dieta = ''.join(sorted(dieta))

    print(dieta)
    i += 1
