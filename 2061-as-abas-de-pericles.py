N, M = map(int, input().split())

for i in range(M):
    if input() == 'fechou':
        N += 1
    else:
        N -=1

print(N)