k = 1                                           # Variavel que conta o número de casos
while True:
    try:
        pos = 0
        num = input()
        ero = input()
        qnt = ero.count(num)                    # Quantidade de subsequencias
        print('Caso #{}:'.format(k))

        if qnt == 0:
            print('Nao existe subsequencia')
            print()
        else:
            pos = ero.rfind(num) +1              # Retornando a ultima posição que o 'num' está em 'ero'
            print('Qtd.Subsequencias:', qnt)
            print('Pos:', pos)
            print()

        k += 1

    except EOFError:
        break