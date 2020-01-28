qnt = int(input())

for i in range(qnt):
    num = list(map(int, input().split()))
    N,K = num[0], num[1]
    if N > K:
        x = N // K
        y = N % K
        result = x + y
    elif N < K:
        result = N
    else:
        result = 1
    print(result)