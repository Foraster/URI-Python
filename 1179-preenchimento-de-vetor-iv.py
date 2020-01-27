par = []
impar = []
for i in range(15):

    valor = int(input())
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)

    if len(par) == 5:
        for j in range(5):
            print("par[{}] = {}".format(j, par[j]))
        par = []

    if len(impar) == 5:
        for k in range(5):
            print("impar[{}] = {}".format(k, impar[k]))
        impar = []

if len(impar) > 0 :
    for k in range(len(impar)):
        print("impar[{}] = {}".format(k, impar[k]))

if len(par) > 0:
    for j in range(len(par)):
        print("par[{}] = {}".format(j, par[j]))
