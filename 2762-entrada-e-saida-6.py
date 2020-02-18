while True:
    try:
        n = [int(x) for x in input().split('.')]
        n.reverse()
        n = '.'.join(str(x) for x in n)
        print(n)

    except EOFError:
        break