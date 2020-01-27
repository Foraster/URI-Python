while True:
    qnt = int(input())
    if qnt == 0:
        break
    for i in range(1, qnt+1):
        if i != qnt:
            print(i, end=" ")
        else:
            print(i)