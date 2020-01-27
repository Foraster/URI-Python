valor = float(input())

cem = valor // 100
resto = valor % 100
cinquenta = resto // 50
resto = resto % 50
vinte = resto // 20
resto = resto % 20
dez = resto // 10
resto = resto % 10
cinco = resto // 5
resto = resto % 5
dois = resto // 2
resto = resto % 2
resto = int(resto)
# MOEDAS:
novoValor = valor * 100
restinho = novoValor % 100
mcinq = restinho // 50
restinho = restinho % 50
mvint = restinho // 25
restinho = restinho % 25
mdez = restinho // 10
restinho = restinho % 10
mcinco = restinho // 5
mum = restinho % 5


print("NOTAS:")
print("%0.0f nota(s) de R$ 100.00" %cem)
print("%0.0f nota(s) de R$ 50.00" %cinquenta)
print("%0.0f nota(s) de R$ 20.00" %vinte)
print("%0.0f nota(s) de R$ 10.00" %dez)
print("%0.0f nota(s) de R$ 5.00" %cinco)
print("%0.0f nota(s) de R$ 2.00" %dois)
print("MOEDAS:")
print("%0.0f moeda(s) de R$ 1.00" %resto)
print("%0.0f moeda(s) de R$ 0.50" %mcinq)
print("%0.0f moeda(s) de R$ 0.25" %mvint)
print("%0.0f moeda(s) de R$ 0.10" %mdez)
print("%0.0f moeda(s) de R$ 0.05" %mcinco)
print("%0.0f moeda(s) de R$ 0.01" %mum)
