vet = []
while True:
    try:
       entrada = input()
       vet.append(entrada)

    except EOFError:
        break

vet = set(vet)
print(len(vet))