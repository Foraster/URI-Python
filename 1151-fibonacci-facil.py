# URI 1151 - Escrito por: Alex Lares
# Algoritmo mostra os primeiros 'N' numeros da sequencia de fibonacci.

N = int(input())
tras = 0
frente = 1

if 0 < N < 46:

    i = 0
    while i < N:

        if i < 1:
            fib = 0

        elif i == 1:
            fib = 1

        else:
            fib = tras + frente
            tras = frente
            frente = fib

        if i == N - 1:
            print(fib)
        else:
            print(fib, end=" ")

        i += 1
