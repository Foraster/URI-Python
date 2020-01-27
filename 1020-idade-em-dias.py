dias = int(input())
ano = dias // 365
resto = dias % 365
mes = resto // 30
dias = resto % 30

print("%d ano(s)" %ano)
print("%d mes(es)" %mes)
print("%d dia(s)" %dias)
