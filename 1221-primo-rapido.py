from math import sqrt

def nPrimo(num):
    for i in range(2, int(sqrt(num))+1):
        if num % i == 0:
            return False
    return True

for i in range(int(input())):
    numero = int(input())
    if nPrimo(numero):
        print('Prime')
    else:
        print('Not Prime')