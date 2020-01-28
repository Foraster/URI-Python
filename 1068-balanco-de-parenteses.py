while True:
    try:
        expressao = input()
        esq = 0
        dir = 0

        for i in range(len(expressao)):
            if expressao[i] == '(':
                esq += 1
            elif expressao[i] == ')':
                dir +=1
                if esq > 0:
                    esq -= 1
                    dir -= 1

        if esq == 0 and dir == 0:
            print('correct')
        else:
            print('incorrect')

    except EOFError:
        break