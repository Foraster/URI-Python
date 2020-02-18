while True:
    try:
        notas = []
        ordem = []
        N, Q = map(int, input().split())

        for i in range(N):
            nota = int(input())
            notas.append(nota)

        notas.sort()
        notas = notas[::-1]
        notas.insert(0,0)

        for j in range(Q):
            pos = int(input())
            ordem.append(pos)

        for k in range(len(ordem)):
            print(notas[ordem[k]])

    except EOFError:
        break