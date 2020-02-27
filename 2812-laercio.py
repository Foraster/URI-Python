for i in range(int(input())):
    n = int(input())
    lista = list(map(int, input().split()))
    lista.sort()
    impares = []
    resultado = []

    # Pegando os valores impares:
    for j in range(n):
        if lista[j] % 2 != 0:
            impares.append(lista[j])

    # Pegando os valores na ordem maior e menor, sucessivamente:
    while len(impares) != 0:
        try:
            resultado.append(impares[len(impares)-1])
            impares.pop()
            resultado.append(impares[0])
            impares.pop(0)
        except IndexError:
            break

    # Printando o resultado:
    if len(resultado) == 0:
        print()
    else:
        for k in range(len(resultado)):
            if k != len(resultado)-1:
                print(resultado[k], end=" ")
            else:
                print(resultado[k])