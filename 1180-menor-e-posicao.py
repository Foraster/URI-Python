qnt = int(input())
vetor = list(map(int, input().split()))
print('Menor valor:', (min(vetor)))

for i in range(qnt):
    if vetor[i] == min(vetor):
        pos = i

print('Posicao:', pos)
