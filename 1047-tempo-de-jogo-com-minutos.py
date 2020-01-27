# Exercicio 1047 URI - 21/03/2019
"""Leia a hora inicial, minuto inicial, hora final e minuto
final de um jogo. A seguir calcule a duração do jogo."""

num = str(input("")).split(" ")

hora_inicial = int(num[0])
minuto_inicial = int(num[1])
hora_final = int(num[2])
minuto_final = int(num[3])
resultado_hora = 0
resultado_minuto = 0

################# HORAS ###########################

resultado_hora = hora_final - hora_inicial
if resultado_hora < 0:
    resultado_hora = 0 #Zera o resultado da hora
    while hora_inicial < 24: #Começa a contar do horario inicial até as 24 horas
        resultado_hora += 1 #Acrescenta uma hora até as 24 horas
        hora_inicial += 1

    resultado_hora += hora_final #Soma da hora inicial até as 24 horas, com a hora final.

if hora_inicial == hora_final and minuto_inicial == minuto_final:
    resultado_hora = 24

################# MINUTOS ###########################

resultado_minuto = minuto_final - minuto_inicial
if resultado_minuto < 0 and resultado_hora != 0:
    resultado_minuto = 0 #Mesmo procedimento da hora, só que até 60
    while minuto_inicial < 60:
        resultado_minuto += 1
        minuto_inicial += 1

    resultado_minuto += minuto_final
    resultado_hora -= 1

if resultado_minuto < 0 and resultado_hora == 0:
    resultado_minuto = 0 #Mesmo procedimento da hora, só que até 60
    while minuto_inicial < 60:
        resultado_minuto += 1
        minuto_inicial += 1

    resultado_minuto += minuto_final
    resultado_hora = 23

print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(resultado_hora, resultado_minuto))
