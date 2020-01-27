qnt = int(input())
i = 0
valor = 0

while i < qnt:
  num = str(input("")).split(" ")

  X = int(num[0])
  Y = int(num[1])

  try:
      valor = X / Y
      print(valor)
  except ZeroDivisionError:
      print("divisao impossivel")

  valor = 0
  i += 1
