# URI 1133 - Escrito por: Alex Lares

X = int(input())
Y = int(input())
valor = 0
temp = 0

if X > Y:
    temp = X
    X = Y
    Y = temp

for valor in range(X+1, Y):
    if ((valor % 5 == 2) or (valor % 5 == 3)):
        print(valor)
