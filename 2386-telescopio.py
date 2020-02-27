A = int(input())
aux = 0

for i in range(int(input())):
    F = int(input())
    if F * A >= 40000000:
        aux += 1

print(aux)