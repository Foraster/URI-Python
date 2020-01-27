x, y = map(float, input().split())

if x > 0:
    if y < 0:
        print('Q4')
    elif y > 0:
        print('Q1')
    else:
        print('Eixo X')

elif x < 0:
    if y < 0:
        print('Q3')
    elif y > 0:
        print('Q2')
    else:
        print('Eixo X')

elif x == 0 and y == 0:
    print('Origem')

else:
    print('Eixo Y')
