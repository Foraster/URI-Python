while True:
    try:
        n = float(input())

        if (0 <= n < 90) or n == 360:
            print("Bom Dia!!")
        elif 90 <= n < 180:
            print("Boa Tarde!!")
        elif 180 <= n < 270:
            print("Boa Noite!!")
        else:
            print("De Madrugada!!")

        horas = int(((n * 240) / 3600) % 60)
        minutos = int(((n * 240) / 60) % 60)
        segundos = round((n * 240) % 60)

        print('%02d:%02d:%02d' % (((horas + 6) % 24), minutos, segundos))

    except EOFError:
        break
