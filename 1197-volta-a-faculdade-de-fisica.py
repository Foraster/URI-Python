while True:
    try:
        n = list(map(int, input().split()))
        c = n[0] * n[1] * 2
        print(c)

    except EOFError:
        break