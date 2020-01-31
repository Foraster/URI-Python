qnt = int(input())
tS, tB, tA = 0,0,0
tS1, tB1, tA1 = 0,0,0

for i in range(qnt):
    nome = input()
    S, B, A = map(int, input().split())
    S1, B1, A1 = map(int, input().split())
    tS += S
    tB += B
    tA += A
    tS1 += S1
    tB1 += B1
    tA1 += A1

print('Pontos de Saque: %.2f' % (tS1*100/tS), end=" %.\n")
print('Pontos de Bloqueio: %.2f' % (tB1*100/tB), end=" %.\n")
print('Pontos de Ataque: %.2f' % (tA1*100/tA), end=" %.\n")
