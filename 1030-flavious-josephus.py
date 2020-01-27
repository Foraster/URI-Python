n = int(input())
vetStr = []

for i in range(1, n+1):

    pessoas, salto = map(int, input().split())
    salto -= 1
    aux = salto
    vetPessoas = []

    for j in range(pessoas):
        vetPessoas.append(j)

    while len(vetPessoas) > 1:
        vetPessoas.pop(aux)
        aux = (aux + salto) % len(vetPessoas)
        if aux > len(vetPessoas):
            aux -= 1

    vetStr.append(str("Case {}: {}".format(i, vetPessoas[0] + 1)))

for x in range(len(vetStr)):
    print(vetStr[x])
