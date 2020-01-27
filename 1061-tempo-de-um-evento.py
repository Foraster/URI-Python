dia_inicial = int(input().split()[1])
tempo_inicial = list(map(int, input().split(' : ')))
hora_inicial, minuto_inicial, segundo_inicial = tempo_inicial[0], tempo_inicial[1], tempo_inicial[2]

dia_final = int(input().split()[1])
tempo_final = list(map(int, input().split(' : ')))
hora_final, minuto_final, segundo_final = tempo_final[0], tempo_final[1], tempo_final[2]

resultado_dia = 0
resultado_hora = 0
resultado_minuto = 0
resultado_segundo = 0

resultado_dia = dia_final - dia_inicial

resultado_hora = hora_final - hora_inicial
if resultado_hora < 0:
    resultado_hora += 24
    resultado_dia -= 1

resultado_minuto = minuto_final - minuto_inicial
if resultado_minuto < 0:
    resultado_minuto += 60
    resultado_hora -= 1

resultado_segundo = segundo_final - segundo_inicial
if resultado_segundo < 0:
    resultado_segundo += 60
    resultado_minuto -= 1

print(resultado_dia, "dia(s)")
print(resultado_hora, "hora(s)")
print(resultado_minuto, "minuto(s)")
print(resultado_segundo, "segundo(s)")
