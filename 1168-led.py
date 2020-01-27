# URI 1168, Escrito por: Alex Lares

qnt = int(input())
i = 0

while i < qnt:

    led = 0
    numero = input()
    lista = list(numero) # Separa numero por numero, criando uma lista
    j = 0

    while j < len(lista):

        if lista[j] == '0':
            led += 6
        elif lista[j] == '1':
            led += 2
        elif lista[j] == '2':
            led += 5
        elif lista[j] == '3':
            led += 5
        elif lista[j] == '4':
            led += 4
        elif lista[j] == '5':
            led += 5
        elif lista[j] == '6':
            led += 6
        elif lista[j] == '7':
            led += 3
        elif lista[j] == '8':
            led += 7
        else: # Caso seja 9
            led += 6

        j += 1

    print(led, "leds")
    i += 1
