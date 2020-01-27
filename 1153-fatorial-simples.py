# URI 1153 - Escrito por: Alex Lares

valor = int(input())
fatorial = 1

for i in range(0, valor):
    fatorial = fatorial * (valor - i)
print(fatorial)

'''
def fatorial(num):
    if num == 0:
        return 1
    else:
        return num*fatorial(num-1)
'''
