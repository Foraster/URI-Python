qnt = int(input())
i = 0

while i < qnt:

    kg = float(input())
    dia = 0

    while True:
        kg = kg / 2
        dia += 1

        if kg <= 1:
            break

    print(dia, "dias")
    i += 1
