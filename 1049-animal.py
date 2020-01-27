animalUm = input().lower()
animalDois = input().lower()
animalTres = input().lower()

if animalUm == "vertebrado":

    if animalDois == "ave":

        if animalTres == "carnivoro":
            print("aguia")

        else:
            print("pomba")

    else:

        if animalTres == "onivoro":
            print("homem")

        else:
            print("vaca")

else:

    if animalDois == "inseto":

        if animalTres == "hematofago":
            print("pulga")

        else:
            print("lagarta")

    else:

        if animalTres == "hematofago":
            print("sanguessuga")

        else:
            print("minhoca")
