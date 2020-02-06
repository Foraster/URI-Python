num = int(input())
tras = 0
frente = 1
icca = []

if 0 < num < 41:

    i = 1
    while i < num+1:

        if i == 1:
            fib = 1

        else:
            fib = tras + frente
            tras = frente
            frente = fib

        icca.append(fib)

        i += 1

icca = icca[::-1]

for i in range(len(icca)):
    if i+1 < len(icca):
        print(icca[i], end=" ")
    else:
        print(icca[i])
print()