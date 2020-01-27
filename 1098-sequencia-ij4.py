i = 0
j = 1
while i <= 2:
    print("I={} J={}".format(i,j))
    j += 1
    if i == 0 and j == 4:
        j = 1.2
        i = 0.2
    elif i == 0.2 and j == 4.2:
        j = 1.4
        i = 0.4
    elif i == 0.4 and j == 4.4:
        j = 1.6
        i = 0.6
    elif i == 0.6 and j == 4.6:
        j = 1.8
        i = 0.8
    elif i == 0.8 and j == 4.8:
        j = 2
        i = 1
    elif i == 1 and j == 5:
        j = 2.2
        i = 1.2
    elif i == 1.2 and j == 5.2:
        j = 2.4
        i = 1.4
    elif i == 1.4 and j == 5.4:
        j = 2.6
        i = 1.6
    elif i == 1.6 and j == 5.6:
        j = 2.8
        i = 1.8
    elif i == 1.8 and j == 5.8:
        j = 3
        i = 2
    elif i == 2 and j == 6:
        i = 2.1
