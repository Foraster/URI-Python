# URI 1073 - Escrito por: Alex Lares

numero = int(input())
i = 2
if numero > 5 and numero < 2000:
    while i <= numero:
        quadrado = i ** 2
        print("{}^2 = {}".format(i, quadrado))
        i += 2
