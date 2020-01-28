qnt = int(input())

for i in range(qnt):
    num = list(map(int, input().split()))
    x, y = num[0], num[1]
    calc = x**y
    print(len(str(calc)))