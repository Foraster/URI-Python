num = 0
quant = 0
maior_numero = 0
posicao = 0
i = 1

while i <= 100:
    num = int(input())
    quant += 1
    if num > maior_numero:
        maior_numero = num
        posicao = quant
    i += 1

print(maior_numero)
print(posicao)
