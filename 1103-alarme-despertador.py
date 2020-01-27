# https://www.urionlinejudge.com.br/judge/pt/problems/view/1103

while True:
    horario = list(map(int, input().split()))
    if horario[0] == 0 and horario[1] == 0 and horario[2] == 0 and horario[3] == 0:
        break
    if horario[0] == 0:
        horario[0] = 24
    if horario[2] == 0:
        horario[2] = 24

    if horario[0] == horario[2] and horario[1] > horario[3]:
        minutos = 1440 - horario[1] + horario[3]

    else:
        if horario[2] < horario[0]:
            horario[2] += 24
        horas = horario[2] - horario[0]
        horas = horas * 60
        minutos = horario[3] - horario[1]
        minutos = horas + minutos
    print(minutos)