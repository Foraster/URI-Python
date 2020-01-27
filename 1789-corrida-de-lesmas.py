while True:
    try:
        qnt = int(input())
        lesmas = list(map(int, input().split()))
        speed = lesmas[0]
        for i in range(len(lesmas)):
            if lesmas[i] > speed:
                speed = lesmas[i]
        if speed < 10:
            print('1')
        elif speed >= 10 and speed < 20:
            print('2')
        else:
            print('3')
    except EOFError:
        break