# URI 1018 - Escrito por: Alex Lares

valor = int(input())

print(valor)

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
um = resto

print(cem, "nota(s) de R$ 100,00")
print(cinquenta, "nota(s) de R$ 50,00")
print(vinte, "nota(s) de R$ 20,00")
print(dez, "nota(s) de R$ 10,00")
print(cinco, "nota(s) de R$ 5,00")
print(dois, "nota(s) de R$ 2,00")
print(um, "nota(s) de R$ 1,00")
