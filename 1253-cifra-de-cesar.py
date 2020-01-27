# Uri 1253, Escrito por: Alex Lares
# chr(97) = a
# ord(a) = 97

qnt = int(input())
i = 0

while i < qnt:
    texto = input().upper()
    numero = int(input())
    qntchar = 0

    if 0 <= numero <= 25:
        for caractere in texto:

            qntchar += 1

            if numero == 0:
                print(texto)
                break
            else:
                letra = ord(caractere)
                cifra = letra - numero

                if cifra < 65: # Se for menor que A, volta pra Z e subtrai
                    cifra = (cifra - 65) + 91
                    novaLetra = chr(cifra)
                    print(novaLetra, end="")
                    if len(texto) - qntchar == 0: # So pula linha se acabou as letras na palavra
                        print()
                else:
                    novaLetra = chr(cifra)
                    print(novaLetra, end="")
                    if len(texto) - qntchar == 0:
                        print()
    i += 1
