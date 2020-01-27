vetor = []
i = 0
j = 0

while i < 20:
    num = int(input())
    vetor.append(num)
    i += 1

vetor.reverse()

for n in vetor:
    print("N[{}] = {}".format(j, n))
    j += 1
