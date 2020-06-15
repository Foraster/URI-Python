for i in range(int(input())):
    anos = 0
    valores = list(map(float, input().split()))
    pop1 = int(valores[0])
    pop2 = int(valores[1])
    cresc1 = valores[2]
    cresc2 = valores[3]
    while True:
        pop1 += cresc1 * (pop1 / 100)
        pop2 += cresc2 * (pop2 / 100)
        anos += 1
        pop1 = int(pop1)
        pop2 = int(pop2)

        if anos > 100:
            print('Mais de 1 seculo.')
            break

        elif pop1 > pop2:
            print(anos, 'anos.')
            break
