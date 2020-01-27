codigo, qnt = map(int, input().split())

if codigo == 1:
    codigo = 4.00
elif codigo == 2:
    codigo = 4.50
elif codigo == 3:
    codigo = 5.00
elif codigo == 4:
    codigo = 2.00
else:
    codigo = 1.50

total = codigo * qnt
print("Total: R$ %.2f" %total)
