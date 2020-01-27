pi = 3.14159
a, b, c = map(float, input().split())

triangulo = (a*c) / 2
print("TRIANGULO: %.3f" %triangulo)

circulo = (c*c) * pi
print("CIRCULO: %.3f" %circulo)

trapezio =  ((a + b) * c) / 2;
print("TRAPEZIO: %.3f" %trapezio)

quadrado = b * b;
print("QUADRADO: %.3f" %quadrado)

retangulo = a * b;
print("RETANGULO: %.3f" %retangulo)
