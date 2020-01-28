x, y, z = map(int, input().split())

if x >= y and x >= z or y <= x and y >= z:
	A = x
	B = y
	C = z
elif y >= x and y >= z or z <= y and x <= y:
	A = y
	B = x
	C = z
elif z >= x and z >= y or x <= z and y <= x:
	A = z
	B = x
	C = y

i = 1
while i > 0:
    if A >= B+C:
        print("Invalido")
        break

    elif A == B and B == C and A == C:
        print("Valido-Equilatero")

    elif A == B or B == C or A == C:
        print("Valido-Isoceles")

    else:
        print("Valido-Escaleno")

    if A*A == B*B + C*C:
        print("Retangulo: S")
    else:
        print("Retangulo: N")

    i -= 1