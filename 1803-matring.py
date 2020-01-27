# NAO TERMINEI
matriz = []
primeiraColuna = []
ultimaColuna = []
for i in range(4):
    linha = []
    num = input()
    lista = list(num)
    for j in range(len(lista)):
        valor = int(lista[j])
        linha.append(valor)
    matriz.append(linha)
    primeiraColuna.append(linha[0])
    ultimaColuna.append(linha[len(linha)-1])
    #print(linha)
    #print(matriz)
    #print(primeiraColuna)
    #print(ultimaColuna)

F = primeiraColuna[0]
L = ultimaColuna[len(ultimaColuna) -1]
N = len(matriz[0])
# tudo certo ate aqui ##############################
#C = coluna 1, 2 ,3..... (C é uma LETRA)
#M[i] = 1 <= i <= N  ====
k = 1
#for k in range(N-1):
#    C = (F * matriz[k] + L) % 257
#    print(C)
print('matriz na posicao K', matriz[k])
print('soma da matriz K', matriz[k])
while k < N-1:
    C = (F * sum(matriz[k]) + L) % 257
    print(C)
    k += 1
