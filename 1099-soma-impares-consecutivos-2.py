qnt = int(input())
i = 0
valor = 0

while i < qnt:
  num = str(input("")).split(" ")

  X = int(num[0])
  Y = int(num[1])

  if Y < X:
      temp = X
      X = Y
      Y = temp

  if X % 2 == 0:
      X += 1
  else:
      X += 2

  while X < Y:
      valor = valor + X
      X += 2

  print (valor)
  valor = 0
  i += 1
