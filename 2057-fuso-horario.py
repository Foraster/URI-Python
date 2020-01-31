S, T, F = map(int, input().split())

if 1 <= (S + T + F) <= 23:
    print(S+T+F)
elif (S + T) > 23:
    print((S+T-24)+F)
elif (S + T + F) < 0:
    print(S+T+F+24)
elif (S + T + F) == 0:
    print('0')
