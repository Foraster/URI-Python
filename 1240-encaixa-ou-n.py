def analisaFinal(listaA, listaB):
    for i in range(len(listaA)):
        if len(listaA) != len(listaB):
            listaA.pop(0)
        elif len(listaA) < len(listaB):
            break
        else:
            break

    if listaA == listaB:
        print('encaixa')
    else:
        print('nao encaixa')


qnt = int(input())

for i in range(qnt):
    num, ero = input().split()
    listNum = list(num)
    listEro = list(ero)

    analisaFinal(listNum, listEro)
