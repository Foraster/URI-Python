def converteRomano(num):
    arab = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roma = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    convertido = ''

    i = 0
    while num > 0:
        for j in range(num // arab[i]):
            convertido += roma[i]
            num -= arab[i]
        i += 1

    return convertido


print(converteRomano(int(input())))
