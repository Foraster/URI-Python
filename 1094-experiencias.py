quantidadeDeCasos = int(input())
total = 0
C = 0
R = 0
S = 0

for i in range(quantidadeDeCasos):
    valor = input().split()
    quantia, tipo = valor
    # Os valores são pegos em string e transformados em inteiros
    total += int(quantia)

    if(tipo == "C"):
        C += int(quantia)
    elif(tipo == "R"):
        R += int(quantia)
    else:
        S += int(quantia)

print("Total: %d cobaias" %total)
print("Total de coelhos:", C)
print("Total de ratos:", R)
print("Total de sapos:", S)
print("Percentual de coelhos: {:.2f} %".format((C/total)*100))
print("Percentual de ratos: {:.2f} %".format((R/total)*100))
print("Percentual de sapos: {:.2f} %".format((S/total)*100))
