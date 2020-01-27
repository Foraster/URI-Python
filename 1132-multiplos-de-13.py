"""Escreva um algoritmo que leia 2 valores inteiros X e Y
calcule a soma dos números que não são múltiplos de 13
entre X e Y, incluindo ambos
Imprima a soma de todos os valores não divisíveis por 13
entre os dois valores lidos na entrada, inclusive ambos se for o caso.."""

X = int(input())
Y = int(input())
soma = 0

if X > Y:
    temp = X
    X = Y
    Y = temp

while X <= Y:
    if X % 13 != 0:
        soma += X
    X += 1

print(soma)
