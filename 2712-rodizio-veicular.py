def checaNum(var):
    var = var[4:8]
    try:
        int(var)
    except ValueError:
        return False
    return True


def checaLetra(var):
    var = var[0:3]
    for k in range(len(var)):
        if not 65 <= ord(var[k]) <= 90:
            return False
    return True


for i in range(int(input())):
    placa = input()

    if len(placa) != 8 or placa[3] != '-':
        print('FAILURE')

    elif not checaLetra(placa):
        print('FAILURE')

    elif not checaNum(placa):
        print('FAILURE')


    else:
        if placa[7] == '1' or placa[7] == '2':
            print('MONDAY')

        elif placa[7] == '3' or placa[7] == '4':
            print('TUESDAY')

        elif placa[7] == '5' or placa[7] == '6':
            print('WEDNESDAY')

        elif placa[7] == '7' or placa[7] == '8':
            print('THURSDAY')

        else:
            print('FRIDAY')

