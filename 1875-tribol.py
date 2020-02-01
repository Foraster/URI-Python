for i in range(int(input())):
    R = 0
    G = 0
    B = 0
    cores = []

    for j in range(int(input())):
        partida = input().split()

        for k in range(2):
            cores.append(partida[k])

    for l in range(0, len(cores), 2):
        if cores[l] == 'R' and cores[l+1] == 'G':
            R += 2
        elif cores[l] == 'R' and cores[l+1] == 'B':
            R += 1
        elif cores[l] == 'G' and cores[l + 1] == 'B':
            G += 2
        elif cores[l] == 'G' and cores[l + 1] == 'R':
            G += 1
        elif cores[l] == 'B' and cores[l + 1] == 'G':
            B += 1
        else:
            B += 2

    if R == G == B:
        print('trempate')

    elif R > G and R > B:
        print('red')

    elif G > R and G > B:
        print('green')

    elif B > R and B > G:
        print('blue')

    elif (R == G) or (R == B) or (G == B):
        print('empate')