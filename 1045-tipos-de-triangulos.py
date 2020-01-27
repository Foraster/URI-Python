x, y, z = map(float, input().split())
if x >= y and x >= z or y <= x and y >= z:
	A = x
	B = y
	C = z
else:
	if y >= x and y >= z or z <= y and x <= y:
		A = y
		B = x
		C = z
	else:
		if z >= x and z >= y or x <= z and y <= x:
			A = z
			B = x
			C = y

if A >= B+C:
	print("NAO FORMA TRIANGULO")

else:
	if A*A == B*B + C*C:
		print("TRIANGULO RETANGULO")

	if A*A > B*B + C*C:
		print("TRIANGULO OBTUSANGULO")

	if A*A < B*B + C*C:
		print("TRIANGULO ACUTANGULO")

	if A == B and B == C and A == C:
		print("TRIANGULO EQUILATERO")

	else:
		if A == B or B == C or A == C:
			print("TRIANGULO ISOSCELES")
