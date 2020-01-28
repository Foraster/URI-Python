while True:
    try:
        qnt = int(input())
        if 2 <= qnt <= 99:
            vetTempo = []
            for i in range(qnt):
                tempo = float(input())
                vetTempo.append(tempo)
            print(min(vetTempo))
    except EOFError:
        break