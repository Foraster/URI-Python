qnt = int(input())

for i in range(qnt):
    ano = int(input())
    if ano == 2015:
        print('1 A.C.')
    elif ano > 2015:
        print(ano-2014, 'A.C.')
    else:
        print(2015-ano, 'D.C.')
