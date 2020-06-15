while True:
    try:
        entrada = input().split(':')
        hora = int(entrada[0])
        minuto = int(entrada[1])
        hora += 1
        if hora > 8:
            while hora > 8:
                hora -= 1
                minuto += 60

        if hora >= 8 and minuto > 0:
            minuto += (hora-8)*60
            print('Atraso maximo:', minuto)
        else:
            print('Atraso maximo: 0')

    except EOFError:
        break