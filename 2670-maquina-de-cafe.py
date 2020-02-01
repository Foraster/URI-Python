A1 = int(input())
A2 = int(input())
A3 = int(input())
menor = []

menor.append((A2 + A2) + (A3 * 4))
menor.append((A1 + A1) + (A3 + A3))
menor.append((A1 * 4) + (A2 + A2))

print(min(menor))