inicio, fim = map(int, input().split())

if 0 <= inicio <= 24 and 0 <= fim <= 24:

    if inicio == fim:
        print('O JOGO DUROU 24 HORA(S)')

    elif inicio > fim:
        resultado = 24 + (fim - inicio)
        print('O JOGO DUROU %d HORA(S)' %resultado)

    else:
        resultado = fim - inicio
        print('O JOGO DUROU %d HORA(S)' %resultado)
