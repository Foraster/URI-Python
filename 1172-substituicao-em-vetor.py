""" Faça um programa que leia um vetor X[10]. Substitua a
seguir, todos os valores nulos e negativos do vetor X por 1.
Em seguida mostre o vetor X.
    Para cada posição do vetor, escreva "X[i] = x",
onde i é a posição do vetor e x é o valor armazenado
naquela posição."""

i = 0

while i < 10:
    num = int(input())
    if num <= 0:
        num = 1
    print('X[{}] = {}'.format(i, num))
    i += 1
