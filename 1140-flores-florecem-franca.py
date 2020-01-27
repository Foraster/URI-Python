# URI 1140, Escrito por: Alex Lares

vetor = []
saida = False

while saida == False:

    # Recebe a frase e a separa palavra por palavra:
    frase = input().strip().lower()
    fraseSeparada = frase.split()

    # Pegando apenas as primeiras letras das palavras:
    for letra in fraseSeparada:
        vetor.append(letra[0])

    # Eliminando letras repetidas:
    novoVetor = set(vetor)

    # Se existe mais de uma letra no vetor, então não é um Tautograma:
    if frase == '*':
        saida = True

    else:

        if len(novoVetor) != 1:
            print('N')
        else:
            print('Y')

    # Zerando as listas:
    vetor = []
    novoVetor = []
