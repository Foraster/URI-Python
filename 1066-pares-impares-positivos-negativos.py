"""Leia 5 valores Inteiros. A seguir mostre quantos valores
digitados foram pares, quantos valores digitados foram ímpares,
quantos valores digitados foram positivos e quantos valores
digitados foram negativos."""

i = 0
par = 0
impar = 0
positivo = 0
negativo = 0

while i < 5:
    valor = int(input())
    if valor % 2 == 0:
        par += 1
    else:
        impar += 1
    if valor > 0:
        positivo += 1
    elif valor < 0:
        negativo += 1
    i += 1

print(par, "valor(es) par(es)")
print(impar, "valor(es) impar(es)")
print(positivo, "valor(es) positivo(s)")
print(negativo, "valor(es) negativo(s)")
