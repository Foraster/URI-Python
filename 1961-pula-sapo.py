P, N = map(int, input().split())
canos = list(map(int, input().split()))
cont = 0

for i in range(len(canos)):
    if i < len(canos)-1:
        if abs(canos[i] - canos[i+1]) > P:
            cont += 1

if cont > 0:
    print('GAME OVER')
else:
    print('YOU WIN')