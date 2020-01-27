# URI 1911

totalDeAlunos = 1
while totalDeAlunos:

    totalDeAlunos = int(input())

    if totalDeAlunos == 0:
        break

    nome = {}

    # Usando os elementos da tupla pra fazer um dicionario:
    for i in range(totalDeAlunos):
        assinatura = input().split()
        nome[assinatura[0]] = assinatura[1]

    alunosPresentes = int(input())
    falsificado = 0
    erro = 0

    for i in range(alunosPresentes):
        j = 0
        assinando = input().split()

        for letra in nome[assinando[0]]:

            if letra != assinando[1][j]:
                erro += 1

            j += 1

        if erro > 1:
            falsificado += 1

        erro = 0

    print(falsificado)
