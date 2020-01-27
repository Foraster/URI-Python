num = int(input())
j = 0

if 2 <= num <= 50:
    for i in range(1000):
        print("N[{}] = {}".format(i, j))
        j += 1
        if j >= num:
            j = 0
