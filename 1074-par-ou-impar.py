# URI 1074 - Escrito por: Alex Lares

qnt = int(input())

for i in range(qnt):

    num = int(input())

    if num == 0:
        print("NULL")

    elif num > 0 and num % 2 == 0:
        print("EVEN POSITIVE")

    elif num > 0 and num % 2 != 0:
        print("ODD POSITIVE")

    elif num < 0 and num % 2 == 0:
        print("EVEN NEGATIVE")

    else:
        print("ODD NEGATIVE")
