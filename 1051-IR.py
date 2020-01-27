salario = float(input())

if salario <= 2000.00:
    print('Isento')

elif salario <= 3000.00:
    novoSalario = (salario-2000.00)*0.08
    print('R$ %.2f' %novoSalario)

elif salario <= 4500.00:
    novoSalario = ((salario-3000.00)*0.18) + (1000.00*0.08)
    print('R$ %.2f' %novoSalario)

else:
    novoSalario = ((salario-4500.00)*0.28) + (1500.00*0.18) + (1000.00*0.08)
    print('R$ %.2f' %novoSalario)
