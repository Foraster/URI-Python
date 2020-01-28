while True:
    x = int(input())
    if x == 0:
        break
    y = 5

    if x % 2 != 0:
        x += 1

    novo = x+2

    while y > 0:
        x += novo
        novo += 2
        y -= 1
    x -= novo
    x += 2
    print(x)