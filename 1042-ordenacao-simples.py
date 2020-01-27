# URI 1042, Escrito por: Alex Lares

x, y, z = map(int, input().split())
vetor = [x, y, z]
i = 0
j = 0

while i < len(vetor):

    j = i + 1
    while j < len(vetor):

        if(vetor[i] > vetor[j]):
            aux = vetor[i]
            vetor[i] = vetor[j]
            vetor[j] = aux

        j += 1

    i += 1

print(vetor[0])
print(vetor[1])
print(vetor[2])
print()
print(x)
print(y)
print(z)
