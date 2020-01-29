certo = int(input())
respostas = list(map(int, input().split()))
cont = 0

for i in range(len(respostas)):
    if respostas[i] == certo:
        cont += 1

print(cont)