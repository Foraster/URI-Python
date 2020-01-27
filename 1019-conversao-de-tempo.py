tempo = int(input())
hora = tempo // 3600
resto = tempo % 3600
minuto = resto // 60
segundo = resto % 60
print("{}:{}:{}".format(hora, minuto, segundo))
