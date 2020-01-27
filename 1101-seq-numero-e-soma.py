while True:
    try:
        a, b = map(int, input().split())

        if a < 1 or b < 1:
            break

        soma = 0
        if a != 0 and b != 0:
            if b > a:
                aux = a
                a = b
                b = aux
            for i in range(b, a+1):
                print(i, end=" ")
                soma += i
            print("Sum={}".format(soma))
        soma = 0
    except:
        break
