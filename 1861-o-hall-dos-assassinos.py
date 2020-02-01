killer = {}
dead = []

while True:
    try:
        nomes = input().split()

        if nomes[0] in killer:
            killer[nomes[0]] += 1
            dead.append(nomes[1])
        else:
            killer[nomes[0]] = 1
            dead.append(nomes[1])

    except EOFError:
        break

for j in dead:
    killer.pop(j, None)

print('HALL OF MURDERERS')
for nome, qnt in killer.items():
    print(nome, qnt)