votos = []

for i in range(int(input())):
    n = int(input())
    votos.append(n)

if votos[0] == max(votos):
    print('S')
else:
    print('N')