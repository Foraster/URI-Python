valores = list(map(int, input().split()))
x, n = valores[0], valores[(len(valores)-1)]
soma = 0

while n >= 0:
    n -= 1
    if n < 0:
        break
    soma += (x + n)

print(soma)