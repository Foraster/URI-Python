def converteHexa(n):
    n = hex(n)
    n = n[2:]
    n = n.upper()
    print(n)

n = converteHexa(int(input()))
