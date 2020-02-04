hobbit = 0
humano = 0
elfo = 0
anao = 0
mago = 0

for i in range(int(input())):
    nome, raca = input().split()

    if raca == 'X':
        hobbit += 1
    elif raca == 'H':
        humano += 1
    elif raca == 'E':
        elfo += 1
    elif raca == 'A':
        anao += 1
    elif raca == 'M':
        mago += 1

print(hobbit, 'Hobbit(s)')
print(humano, 'Humano(s)')
print(elfo, 'Elfo(s)')
print(anao, 'Anao(s)')
print(mago, 'Mago(s)')