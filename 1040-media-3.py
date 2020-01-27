n1, n2, n3, n4 = map(float, input().split())
media = ((n1*2) + (n2*3) + (n3*4) + (n4*1)) / 10
print("Media: %.1f" %media)

if 5.0 <= media < 7.0:
    print('Aluno em exame.')
    n5 = float(input())
    print('Nota do exame: %.1f' %n5)
    mediaFinal = (media + n5) / 2

    if mediaFinal >= 5.0:
        print("Aluno aprovado.")
    else:
        print('Aluno reprovado.')

    print('Media final: %.1f' %mediaFinal)

elif media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print('Aluno reprovado.')
