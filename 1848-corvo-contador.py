soma = 0
for i in range(3):
    while True:
        entrada = input()
        if entrada == 'caw caw':
            print(soma)
            soma = 0
            break

        if entrada == '---':
            soma += 0
        elif entrada == '--*':
            soma += 1
        elif entrada == '-*-':
            soma += 2
        elif entrada == '-**':
            soma += 3
        elif entrada == '*--':
            soma += 4
        elif entrada == '*-*':
            soma += 5
        elif entrada == '**-':
            soma += 6
        elif entrada == '***':
            soma += 7