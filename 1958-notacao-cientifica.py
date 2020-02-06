num = float(input())
ero = str(num)

if num < 0 or ero[0] == '-':
    print('{:.4E}'.format(num))

else:
    print('+', end="")
    print('{:.4E}'.format(num))