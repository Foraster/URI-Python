i = 1
j = 7
while i <= 9:
    print("I={} J={}".format(i,j))
    j -= 1
    if j == 4:
        j = 9
        i += 2
    if i == 3 and j == 6:
        j = 11
        i += 2
    if i == 5 and j == 8:
        j = 13
        i += 2
    if i == 7 and j == 10:
        j = 15
        i += 2
    if i == 9 and j == 12:
        i += 1
