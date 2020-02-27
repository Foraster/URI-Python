for i in range(int(input())):
    soma = 0
    for j in range(int(input())):
        palavra = input()
        for k in range(len(palavra)):
            soma += (ord(palavra[k]) -65) + j + k
    print(soma)