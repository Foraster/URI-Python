col = int(input())
op = input()

# Criando a Matriz 12x12:
matriz = []

for i in range(12):
    linhaTemp = []
    for j in range(12):
        valor = float(input())
        linhaTemp.append(valor)
    matriz.append(linhaTemp)

coluna = [x[col] for x in matriz]
soma = sum(coluna)
media = soma/12

# Resposta:
if op == 'S' or op == 's':
    print("%.1f" % soma)

if op == 'M' or op == 'm':
    print("%.1f" % media)