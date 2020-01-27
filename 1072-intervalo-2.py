qnt = int(input())
i = 0
dentro = 0
fora = 0

while i < qnt:
    num = int(input())
    if num >= 10 and num <= 20:
        dentro += 1
    else:
        fora += 1
    i += 1

print(dentro, 'in')
print(fora, 'out')
