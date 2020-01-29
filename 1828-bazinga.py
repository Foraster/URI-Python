qnt = int(input())

for i in range(1, qnt+1):
    sheldon, raj = map(str, input().split())
    var = 0

    if sheldon == 'tesoura' and raj == 'papel':
        var = 1
    elif sheldon == 'papel' and raj == 'tesoura':
        var = 2

    elif sheldon == 'papel' and raj == 'pedra':
        var = 1
    elif sheldon == 'pedra' and raj == 'papel':
        var = 2

    elif sheldon == 'pedra' and raj == 'lagarto':
        var = 1
    elif sheldon == 'lagarto' and raj == 'pedra':
        var = 2

    elif sheldon == 'lagarto' and raj == 'Spock':
        var = 1
    elif sheldon == 'Spock' and raj == 'lagarto':
        var = 2

    elif sheldon == 'Spock' and raj == 'tesoura':
        var = 1
    elif sheldon == 'tesoura' and raj == 'Spock':
        var = 2

    elif sheldon == 'tesoura' and raj == 'lagarto':
        var = 1
    elif sheldon == 'lagarto' and raj == 'tesoura':
        var = 2

    elif sheldon == 'lagarto' and raj == 'papel':
        var = 1
    elif sheldon == 'papel' and raj == 'lagarto':
        var = 2

    elif sheldon == 'papel' and raj == 'Spock':
        var = 1
    elif sheldon == 'Spock' and raj == 'papel':
        var = 2

    elif sheldon == 'Spock' and raj == 'pedra':
        var = 1
    elif sheldon == 'pedra' and raj == 'Spock':
        var = 2

    elif sheldon == 'pedra' and raj == 'tesoura':
        var = 1
    elif sheldon == 'tesoura' and raj == 'pedra':
        var = 2

    else:
        var = 3

    if var == 1:
        print('Caso #{}: Bazinga!'.format(i))
    elif var == 2:
        print('Caso #{}: Raj trapaceou!'.format(i))
    else:
        print('Caso #{}: De novo!'.format(i))