qnt = int(input())

for i in range(qnt):
    num = list(map(int, input().split()))
    x, y = num[0], num[1]

    if x % 2 == 0:
        x += 1

    novo = x+2

    while y > 0:
        x += novo
        novo += 2
        y -= 1
    x -= novo
    x += 2
    print(x)