qnt = int(input())
resultado = []

for i in range(qnt):
    frase = input()
    lista = []
    for letra in frase:
        lista.append(letra)

    # Primeira passada: pula 3 casas de cada letra.
    for i in range(len(lista)):
        if 65 <= ord(lista[i]) <= 90 or 97 <= ord(lista[i]) <= 122:
            lista[i] = chr(ord(lista[i]) + 3)

    # Segunda passada: inverte a lista.
    lista.reverse()

    # Terceira passada: todos os caracteres a partir do meio volta 1 casa.
    metade1 = lista[0:int(len(lista)/2)]
    metade2 = lista[int(len(lista)/2):int(len(lista))]

    for j in range(len(metade2)):
        metade2[j] = chr(ord(metade2[j])-1)

    # Juntando tudo e guardando num vetor de resultados
    lista = metade1+metade2
    cripto = ''.join(lista)
    resultado.append(cripto)

# Printando todos os resultados:
for x in range(len(resultado)):
    print(resultado[x])