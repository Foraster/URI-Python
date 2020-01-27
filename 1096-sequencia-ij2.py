i = 1
j = 7
while i <= 9 and j > 4:
    print("I={} J={}".format(i,j))
    j -= 1
    if j == 4:
        j = 7
        i += 2
