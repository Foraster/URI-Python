qnt = int(input())
maior = 0.0
escolhido = -1

for i in range(qnt):
    matricula, nota = input().split()
    matricula, nota = int(matricula), float(nota)
    if nota >= 8 and nota > maior:
        maior = nota
        escolhido = matricula

if escolhido >= 0:
    print(escolhido)
else:
    print('Minimun note not reached')
