X = int(input())
Y = int(input())
valor = 0
temp = 0

if Y < X:
    temp = X
    X = Y
    Y = temp

if X % 2 == 0:
    X += 1
else:
    X += 2

while X < Y:
    valor = valor+ X
    X += 2

print(valor)
