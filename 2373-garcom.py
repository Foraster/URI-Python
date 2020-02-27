qntCopos = 0
for i in range(int(input())):
    num = list(map(int, input().split()))
    if num[0] > num[1]:
        qntCopos += num[1]
print(qntCopos)