qnt = int(input())

for i in range(qnt):
    fibo = [0,1]
    valor = int(input())
    if valor > 1:
        for j in range(2 , valor+1):
            fibo.append(fibo[j-2]+fibo[j-1])
        print('Fib({}) = {}'.format(valor, fibo[valor]))

    else:
        print('Fib({}) = {}'.format(valor, fibo[valor]))
