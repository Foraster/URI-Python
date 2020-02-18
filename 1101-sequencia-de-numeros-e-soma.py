while True:
    soma = 0
    M, N = map(int, input().split())
    if M <= 0 or N <= 0:
        break

    if M > N:
        N, M = M, N

    for i in range(M, N+1):
        print(i, end=" ")
        soma += i
    print('Sum={}'.format(soma))
