qnt = int(input())

for i in range(qnt):
    pessoa = input().split()
    n1, n2 = map(int, input().split())
    soma = n1 + n2

    if soma % 2 == 0:
        par = pessoa.index("PAR")
        print(pessoa[par - 1])
    else:
        impar = pessoa.index("IMPAR")
        print(pessoa[impar -1])
