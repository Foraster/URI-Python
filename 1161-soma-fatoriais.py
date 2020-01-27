def fatorial(num):
    if num == 0:
        return 1
    else:
        return num*fatorial(num-1)

while True:
    try:
        a, b = map(int, input().split())
        soma = fatorial(a) + fatorial(b)
        print(soma)
    except EOFError:
        break
