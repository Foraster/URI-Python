def converteHexa(x):
    x = hex(x)
    x = x[2:]
    x = x.upper()
    x = '0x' + str(x)
    print(x)


while True:
    try:
        n = input().lower()
        if n == '-1':
            break
        n = int(n)
        converteHexa(n)
    except ValueError:
        n = int(n, 16)
        print(n)
