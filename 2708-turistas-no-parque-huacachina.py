turistas = 0
carros = 0

while True:
    entrada = input().split()
    print(entrada)

    if entrada[0] == 'ABEND':
        break

    elif entrada[0] == 'SALIDA':
        turistas += int(entrada[1])
        carros += 1

    elif entrada[0] == 'VUELTA':
        turistas -= int(entrada[1])
        carros -= 1

print(turistas)
print(carros)