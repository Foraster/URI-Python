salario = float(input())

if 0 <= salario <= 400.00:
    novoSalario = salario + (salario * 0.15)
    reajuste = salario * 0.15
    print('Novo salario: %.2f' %novoSalario)
    print('Reajuste ganho: %.2f' %reajuste)
    print('Em percentual: 15 %')
elif salario <= 800.00:
    novoSalario = salario + (salario * 0.12)
    reajuste = salario * 0.12
    print('Novo salario: %.2f' %novoSalario)
    print('Reajuste ganho: %.2f' %reajuste)
    print('Em percentual: 12 %')
elif salario <= 1200.00:
    novoSalario = salario + (salario * 0.10)
    reajuste = salario * 0.10
    print('Novo salario: %.2f' %novoSalario)
    print('Reajuste ganho: %.2f' %reajuste)
    print('Em percentual: 10 %')
elif salario <= 2000.00:
    novoSalario = salario + (salario * 0.07)
    reajuste = salario * 0.07
    print('Novo salario: %.2f' %novoSalario)
    print('Reajuste ganho: %.2f' %reajuste)
    print('Em percentual: 7 %')
else:
    novoSalario = salario + (salario * 0.04)
    reajuste = salario * 0.04
    print('Novo salario: %.2f' %novoSalario)
    print('Reajuste ganho: %.2f' %reajuste)
    print('Em percentual: 4 %')
