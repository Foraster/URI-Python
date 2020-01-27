soma = 0
linha = int(input())
T = input().upper()

for i in range(12):
    for j in range(12):
        valor = float(input())
        if(i == linha):
            soma += valor

if T == 'S':
    print("%.1f" %soma)

elif T == 'M':
    print("%.1f" %(soma/12))
