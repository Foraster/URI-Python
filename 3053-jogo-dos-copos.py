qnt = int(input())
pos = input()
copos = ['A', 'B', 'C']

for i in range(qnt):
    num = int(input())

    if num == 1:
        copos[0], copos[1] = copos[1], copos[0]
    elif num == 2:
        copos[1], copos[2] = copos[2], copos[1]
    elif num == 3:
        copos[0], copos[2] = copos[2], copos[0]

if copos.index(pos) == 0:
    print('A')
elif copos.index(pos) == 1:
    print('B')
elif copos.index(pos) == 2:
    print('C')
