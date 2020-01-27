vetor = []
for i in range(100):
    valor = float(input())
    vetor.append(valor)
    if vetor[i] <= 10:
        print("A[{}] = {:.1f}".format(i, valor))
