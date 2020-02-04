data, limite = map(int, input().split())

if data > limite:
    print('Eu odeio a professora!')

elif limite - data >= 3:
    print('Muito bem! Apresenta antes do Natal!')

elif limite - data < 3:
    print('Parece o trabalho do meu filho!')

    if data + 2 >= 24:
        print('Fail! Entao eh nataaaaal!')
    else:
        print('TCC Apresentado!')