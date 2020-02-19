resultado = 0
for i in range(int(input())):
    t,v = map(int, input().split())
    resultado += t * v
print(resultado)