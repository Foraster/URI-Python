import math
while True:
    valores = list(map(int, input().split()))
    if valores[0] == 0:
        break
    else:
        a = valores[0]
        b = valores[1]
        c = valores[2]

        calc = math.sqrt(a * b * (100/c))
        print(int(calc))