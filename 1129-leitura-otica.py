while True:
    qnt = int(input())
    if qnt == 0:
        break

    for i in range(qnt):
        a, b, c, d, e = map(int, input().split())
        cont = 0

        if a <= 127:
            cont += 1
        if b <= 127:
            cont += 7
        if c <= 127:
            cont += 18
        if d <= 127:
            cont += 29
        if e <= 127:
            cont += 50

        if cont != 1 and cont != 7 and cont != 18 and cont != 29 and cont != 50:
            print('*')
        elif cont == 1:
            print('A')
        elif cont == 7:
            print('B')
        elif cont == 18:
            print('C')
        elif cont == 29:
            print('D')
        elif cont == 50:
            print('E')
