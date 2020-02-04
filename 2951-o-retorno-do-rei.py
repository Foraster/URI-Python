N, G = map(int, input().split())
runas = {}
amizade = 0

for i in range(N):
    entrada = input().split()
    runas[entrada[0]] = int(entrada[1])

qnt = int(input())
letras = list(map(str, input().split()))

for j in range(len(letras)):
    if letras[j] in runas:
        amizade += runas[letras[j]]

print(amizade)
if amizade >= G:
    print('You shall pass!')
else:
    print('My precioooous')