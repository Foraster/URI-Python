while True:
    try:
        n = int(input())

        if (0 <= n <= 89) or n == 360:
            print("Bom Dia!!")
        elif (90 <= n <= 179):
            print("Boa Tarde!!")
        elif (180 <= n <= 269):
            print("Boa Noite!!")
        else:
            print("De Madrugada!!")

    except EOFError:
        break